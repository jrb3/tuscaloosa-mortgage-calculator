# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains a single-file HTML mortgage calculator specifically designed for Tuscaloosa County, Alabama properties. The calculator is a standalone web application that includes:

- HTML structure and CSS styling
- JavaScript functionality for mortgage calculations
- Tuscaloosa County-specific property tax calculations using millage rates
- Responsive design for mobile and desktop use

## Architecture

**Single File Application**: The entire application is contained in `tuscaloosa-mortgage-calculator.html` with inline CSS and JavaScript.

**Key Components**:
- Form inputs for mortgage parameters (home price, down payment, interest rate, loan term)
- Tuscaloosa County tax rate options (33 mills county average, 46 mills county median, 53 mills city rate)
- Real-time PMI calculation based on down payment percentage
- Comprehensive results display with payment breakdown

**Tax Calculation Logic**:
- Uses Alabama's property tax formula: (Appraised Value × 10% Assessment Rate) × Millage Rate
- Millage rates are specific to Tuscaloosa County jurisdictions
- Supports custom millage rate input

## Development

**No Build Process**: This is a static HTML file that can be opened directly in a browser.

**Testing**: Open `tuscaloosa-mortgage-calculator.html` in a web browser to test functionality.

**Key Features**:
- Auto-calculation of PMI when down payment < 20%
- Dynamic form validation
- Responsive grid layout
- Alabama-specific property tax calculations

## Development Environment

**VS Code Setup**: Full VS Code workspace configuration is available with:
- Custom code snippets for mortgage calculator patterns (prefix: `mort-*`)
- Chrome debugger configurations for HTML debugging
- Live Server integration (Ctrl+Shift+L to launch)
- Python debugging configurations
- Custom tasks for running servers and Python scripts

**MCP Servers Configured**:
- GitHub - Repository management and PR reviews
- Filesystem - Enhanced file operations
- Context7 - Up-to-date library/framework documentation

**Python Environment**:
- Virtual environment located at `.venv/`
- Python interpreter: `.venv/bin/python`
- Configured for Black formatting and Flake8 linting

## Testing & Debugging

**Live Server** (Recommended):
- Press `Ctrl+Shift+L` in VS Code to start Live Server
- Automatically opens browser at `http://localhost:5500`
- Auto-reloads on file changes

**Chrome Debugging**:
- Press `F5` to launch Chrome with debugger attached
- Set breakpoints in JavaScript code
- Step through mortgage calculations

**Python HTTP Server** (Alternative):
```bash
python -m http.server 8000
# Then open http://localhost:8000/tuscaloosa-mortgage-calculator.html
```

## Available Code Snippets

Type these prefixes in VS Code and press Tab:
- `mort-input` - Form input field template
- `mort-select` - Select dropdown template
- `mort-result` - Result display section
- `mort-calc` - Calculation function template
- `mort-altax` - Alabama property tax calculation
- `mort-pmi` - PMI calculation logic
- `mort-payment` - Mortgage payment formula
- `mort-currency` - Currency formatting function

## File Structure

```
/
├── tuscaloosa-mortgage-calculator.html     # Main application file
├── tuscaloosa-mortgage-calculator.code-workspace  # VS Code workspace
├── CLAUDE.md                               # This file - Claude Code instructions
├── .mcp.json                               # MCP server configuration
├── .vscode/                                # VS Code configuration
│   ├── settings.json                       # Editor settings
│   ├── extensions.json                     # Recommended extensions
│   ├── tasks.json                          # Build/run tasks
│   ├── launch.json                         # Debug configurations
│   ├── keybindings.json                    # Custom keyboard shortcuts
│   └── html.code-snippets                  # Code snippets
├── .venv/                                  # Python virtual environment
└── landing-page/                           # Additional web content
```