---
name: update-tax-rates
description: Update Tuscaloosa County property tax millage rates in the mortgage calculator
---

# Update Tax Rates Skill

This skill helps you update the property tax millage rates in the Tuscaloosa County Mortgage Calculator with the most current data.

## Purpose

Property tax millage rates change periodically. This skill automates the process of:
1. Researching current Tuscaloosa County millage rates
2. Updating the rates in the HTML calculator
3. Documenting the source and date of the update
4. Testing the calculator with updated rates

## Parameters

- `--source <url>`: Optional URL to official tax rate source
- `--year <yyyy>`: Optional year for the tax rates (default: current year)
- `--test`: Run test calculations after updating rates

## Workflow

1. **Research Current Rates**
   - Search for official Tuscaloosa County tax assessor data
   - Verify rates from tuscaloosa-al.gov or TCTA website
   - Note the effective date and source

2. **Identify Rate Locations in Code**
   - Read `tuscaloosa-mortgage-calculator.html`
   - Locate the millage rate dropdown options (around line 45-50)
   - Find the calculation logic that uses these rates (around line 180)

3. **Update Rates**
   - Update the three standard options:
     - County average (currently 33 mills)
     - County median (currently 46 mills)
     - City rate (currently 53 mills)
   - Ensure rates are in the correct unit (mills = dollars per $1,000 assessed value)

4. **Document the Update**
   - Add an HTML comment with:
     - Update date
     - Source of rates
     - Effective tax year

   Example:
   ```html
   <!-- Tax rates updated: 2025-12-29 -->
   <!-- Source: Tuscaloosa County Tax Assessor -->
   <!-- Effective: Tax Year 2025 -->
   ```

5. **Test the Calculator**
   - Calculate a sample mortgage with each rate option
   - Verify the monthly tax amounts are reasonable
   - Check that custom rate input still works

6. **Verify Formula**
   - Confirm Alabama property tax formula is still correct:
     `(Appraised Value × 10% Assessment Rate) × Millage Rate`

## Example Usage

```bash
# Basic usage (will research current rates)
/update-tax-rates

# With specific source
/update-tax-rates --source https://example.com/tax-rates-2025

# With testing
/update-tax-rates --test
```

## Expected Output

After running this skill, you should have:
- Updated millage rates in the calculator
- Documentation comments in the HTML
- Test results showing the calculator works correctly
- A summary of what was changed

## Notes

- Always verify rates from official sources
- Tuscaloosa County reconstitutes rates annually
- City of Tuscaloosa and county rates may differ
- School district rates can vary by location

## Related Files

- `tuscaloosa-mortgage-calculator.html` - Main calculator file (lines 45-50, 180+)
- Test the calculator at `http://localhost:5500` using Live Server
