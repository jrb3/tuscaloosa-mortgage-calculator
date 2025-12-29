
"""
r40_russell3000_screen.py

Purpose
-------
Build a Rule-of-40 screen (Alex Karp / Palantir definition: YoY revenue growth + *adjusted* operating margin)
for the Russell 3000 universe. Because "adjusted operating margin" is not standardized across companies,
this script approximates it as:

    adjusted_op_margin_TTM = (operating_income_TTM + stock_based_comp_TTM) / revenue_TTM

If SBC data is missing, we fall back to GAAP operating margin:

    fallback_op_margin_TTM = operating_income_TTM / revenue_TTM

Revenue growth is computed on a TTM basis:

    revenue_growth_yoy = (revenue_TTM / revenue_TTM_prior) - 1

Universe
--------
- Pulls holdings for iShares Russell 3000 ETF (IWV) as a practical proxy for the Russell 3000 constituents.
  (Official FTSE Russell constituent spreadsheets are available from LSEG/FTSE, usually after rebalances.)

Data Source
-----------
- Financial Modeling Prep (FMP) Fundamentals API (free key available): https://site.financialmodelingprep.com/developer/docs
  You must set your API key via environment variable FMP_API_KEY or pass --api-key.

Outputs
-------
- r3000_rule_of_40.csv : per‑ticker results
- r3000_rule_of_40.xlsx: formatted spreadsheet
- r3000_rule_of_40_ge40.csv : screened list (Rule of 40 >= 40)

Usage
-----
python r40_russell3000_screen.py --period quarterly --universe iwv --min-score 40 --threads 4

Notes
-----
- "Adjusted" operating margin here only adds back SBC (and ignores employer payroll tax on SBC);
  company‑specific non‑GAAP adjustments will differ from this approximation.
- If you have an official Russell 3000 constituent file, you may pass it with --tickers-csv having columns: Ticker,Name.
"""

import argparse
import csv
import io
import math
import os
import sys
import time
from dataclasses import dataclass
from typing import Optional, List, Dict, Tuple

import requests
import pandas as pd

IWV_HOLDINGS_CSV = "https://www.ishares.com/us/products/239714/ishares-russell-3000-etf/1467271812596.ajax?dataType=fund&fileName=IWV_holdings&fileType=csv"

def fetch_iwv_universe() -> pd.DataFrame:
    """Download IWV holdings CSV and return equity tickers & names."""
    resp = requests.get(IWV_HOLDINGS_CSV, timeout=30)
    resp.raise_for_status()
    df = pd.read_csv(io.StringIO(resp.text))
    # Normalize columns
    cols = {c.lower().strip().replace(" ", "_"): c for c in df.columns}
    # Keep equities only, drop cash, futures, etc. The file typically has 'Asset Class' and 'Ticker'/'Name' columns.
    # Try to be robust to minor schema changes.
    # Identify column names
    ticker_col = next((c for c in df.columns if c.lower().strip() in ("ticker", "ticker_")), None)
    name_col = next((c for c in df.columns if c.lower().strip() in ("name",)), None)
    asset_col = next((c for c in df.columns if c.lower().strip() in ("asset class", "asset_class")), None)
    if ticker_col is None or name_col is None:
        raise RuntimeError("Could not find Ticker/Name columns in IWV CSV.")
    if asset_col and asset_col in df.columns:
        df = df[df[asset_col].astype(str).str.lower().str.contains("equity", na=False)]
    # Basic clean/ticker normalization
    df = df[[ticker_col, name_col]].dropna()
    df[ticker_col] = df[ticker_col].astype(str).str.upper().str.replace(".", "-", regex=False)  # BRK.B -> BRK-B
    df = df[~df[ticker_col].str.contains("^CASH", na=False)]
    df = df[~df[ticker_col].str.contains("FUT|^X$", na=False)]
    df = df.drop_duplicates(subset=[ticker_col])
    df = df.rename(columns={ticker_col: "Ticker", name_col: "Name"}).reset_index(drop=True)
    return df

def chunked(iterable, n):
    for i in range(0, len(iterable), n):
        yield iterable[i:i+n]

def get_json(url: str, params: Dict[str, str], max_retries: int = 3) -> Optional[List[Dict]]:
    for attempt in range(max_retries):
        try:
            r = requests.get(url, params=params, timeout=30)
            if r.status_code == 200:
                return r.json()
        except Exception:
            pass
        time.sleep(1 + attempt)
    return None

def ttm_from_quarters(values: List[float]) -> Optional[float]:
    vals = [v for v in values if isinstance(v, (int, float)) and not math.isnan(v)]
    if len(vals) < 4:
        return None
    return sum(vals[:4])

def compute_metrics(symbol: str, api_key: str) -> Dict[str, Optional[float]]:
    """
    Return dict with revenue_ttm, revenue_ttm_prior, sbc_ttm, op_inc_ttm, adj_op_margin, op_margin, growth_yoy, rule40_est.
    """
    base = "https://financialmodelingprep.com/api/v3"
    # Income statements quarterly for TTM
    inc = get_json(f"{base}/income-statement/{symbol}", {"period": "quarter", "limit": "8", "apikey": api_key})
    if not inc or not isinstance(inc, list) or len(inc) == 0:
        return {"ok": False}
    # Pull revenue, operatingIncome, stockBasedCompensation (if present)
    rev = [row.get("revenue") or row.get("salesRevenueNet") for row in inc]
    opi = [row.get("operatingIncome") for row in inc]
    sbc = [row.get("stockBasedCompensation") for row in inc]
    # Compute TTM and prior TTM
    rev_ttm = ttm_from_quarters(rev)
    opi_ttm = ttm_from_quarters(opi)
    sbc_ttm = ttm_from_quarters(sbc)
    rev_prior = ttm_from_quarters(rev[4:])  # previous 4 quarters
    growth = None
    if rev_ttm and rev_prior and rev_prior != 0:
        growth = (rev_ttm / rev_prior) - 1.0
    # Compute margins
    adj_op_margin = None
    op_margin = None
    if rev_ttm and rev_ttm != 0:
        if opi_ttm is not None and sbc_ttm is not None:
            adj_op_margin = (opi_ttm + sbc_ttm) / rev_ttm
        if opi_ttm is not None:
            op_margin = opi_ttm / rev_ttm
    # Rule of 40 (estimated)
    rule40 = None
    # Prefer adjusted margin when available, else fallback to GAAP
    margin_used = None
    if growth is not None:
        if adj_op_margin is not None:
            rule40 = (growth + adj_op_margin) * 100.0
            margin_used = "adjusted"
        elif op_margin is not None:
            rule40 = (growth + op_margin) * 100.0
            margin_used = "gaap"
    return {
        "ok": True,
        "revenue_ttm": rev_ttm,
        "revenue_ttm_prior": rev_prior,
        "sbc_ttm": sbc_ttm,
        "operating_income_ttm": opi_ttm,
        "growth_yoy_pct": None if growth is None else growth * 100.0,
        "adj_op_margin_pct": None if adj_op_margin is None else adj_op_margin * 100.0,
        "gaap_op_margin_pct": None if op_margin is None else op_margin * 100.0,
        "rule40_score": rule40,
        "margin_basis": margin_used,
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--api-key", default=os.getenv("FMP_API_KEY", ""), help="FMP API key (or set FMP_API_KEY env var)")
    ap.add_argument("--tickers-csv", default="", help="Optional CSV with columns: Ticker,Name to override IWV universe")
    ap.add_argument("--min-score", type=float, default=40.0, help="Minimum Rule of 40 score to keep in the screened output")
    ap.add_argument("--sleep", type=float, default=0.25, help="Delay between calls to respect rate limits")
    args = ap.parse_args()
    if not args.api_key:
        print("ERROR: Provide FMP API key via --api-key or FMP_API_KEY env var.", file=sys.stderr)
        sys.exit(1)

    if args.tickers_csv and os.path.exists(args.tickers_csv):
        universe = pd.read_csv(args.tickers_csv).dropna()
        universe = universe.rename(columns=lambda c: c.strip())
        if not {"Ticker", "Name"}.issubset(universe.columns):
            raise SystemExit("tickers-csv must have columns: Ticker,Name")
    else:
        print("Downloading IWV holdings as a Russell 3000 proxy...")
        universe = fetch_iwv_universe()
    print(f"Universe size: {len(universe)}")

    rows = []
    count = 0
    for _, row in universe.iterrows():
        symbol = row["Ticker"]
        name = row["Name"]
        count += 1
        if count % 25 == 0:
            print(f"Processed {count} / {len(universe)}...")
        try:
            metrics = compute_metrics(symbol, args.api_key)
            time.sleep(args.sleep)
            if not metrics.get("ok"):
                rows.append({
                    "Ticker": symbol, "Name": name, "growth_yoy_pct": None,
                    "adj_op_margin_pct": None, "gaap_op_margin_pct": None,
                    "rule40_score": None, "margin_basis": None
                })
                continue
            out = {
                "Ticker": symbol,
                "Name": name,
                "Growth YoY % (TTM)": metrics["growth_yoy_pct"],
                "Adjusted Op Margin % (TTM)": metrics["adj_op_margin_pct"],
                "GAAP Op Margin % (TTM)": metrics["gaap_op_margin_pct"],
                "Rule of 40 Score": metrics["rule40_score"],
                "Margin Basis Used": metrics["margin_basis"],
            }
            rows.append(out)
        except Exception as e:
            rows.append({
                "Ticker": symbol, "Name": name, "growth_yoy_pct": None,
                "adj_op_margin_pct": None, "gaap_op_margin_pct": None,
                "rule40_score": None, "margin_basis": None
            })

    df = pd.DataFrame(rows)
    # Sort by score desc
    if "Rule of 40 Score" in df.columns:
        df = df.sort_values(by="Rule of 40 Score", ascending=False, na_position="last")
    # Save
    df.to_csv("r3000_rule_of_40.csv", index=False)
    try:
        df.to_excel("r3000_rule_of_40.xlsx", index=False)
    except Exception:
        pass
    # Screened
    screener = df[df["Rule of 40 Score"].astype(float) >= args.min_score] if "Rule of 40 Score" in df.columns else pd.DataFrame()
    screener.to_csv("r3000_rule_of_40_ge40.csv", index=False)
    print("Saved: r3000_rule_of_40.csv, r3000_rule_of_40.xlsx, r3000_rule_of_40_ge40.csv")
    if not screener.empty:
        print(f"{len(screener)} names with Rule of 40 >= {args.min_score}.")

if __name__ == "__main__":
    main()
