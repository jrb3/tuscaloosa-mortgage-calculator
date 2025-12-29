# Tuscaloosa County Mortgage Calculator

A comprehensive, web-based mortgage calculator specifically designed for properties in Tuscaloosa County, Alabama. This tool provides accurate mortgage payment estimates including principal, interest, property taxes, insurance, and PMI.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

### Mortgage Calculations
- **Principal & Interest**: Standard amortization formula for accurate monthly payments
- **Property Taxes**: Alabama-specific calculations using 10% assessment rate and local millage rates
- **Homeowners Insurance**: Customizable annual insurance costs
- **PMI (Private Mortgage Insurance)**: Automatic calculation when down payment < 20%

### Tuscaloosa County Tax Rates
Pre-configured with accurate local millage rates:
- **County Average**: 33 mills
- **County Median**: 46 mills
- **City Rate**: 53 mills
- **Custom Rate**: Enter your specific millage rate

### User Experience
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Real-time Calculations**: Instant updates as you adjust parameters
- **Clean Interface**: Modern, accessible design with clear visual hierarchy
- **Comprehensive Breakdown**: Detailed display of all payment components

## Demo

Open `tuscaloosa-mortgage-calculator.html` in any modern web browser to use the calculator.

## Quick Start

### Option 1: Direct Use (No Installation Required)

Simply download and open the HTML file:

```bash
git clone https://github.com/jrb3/tuscaloosa-mortgage-calculator.git
cd tuscaloosa-mortgage-calculator
open tuscaloosa-mortgage-calculator.html  # macOS
# or
xdg-open tuscaloosa-mortgage-calculator.html  # Linux
# or double-click the file in Windows
```

### Option 2: Local Development Server

Using Python:
```bash
python -m http.server 8000
# Open http://localhost:8000/tuscaloosa-mortgage-calculator.html
```

Using VS Code Live Server (Recommended for Development):
1. Install the "Live Server" extension
2. Open the project in VS Code
3. Right-click `tuscaloosa-mortgage-calculator.html`
4. Select "Open with Live Server"
5. Or press `Ctrl+Shift+L`

## Development Environment Setup

This project includes comprehensive VS Code configuration and MCP (Model Context Protocol) server integration for enhanced development with Claude Code.

### Prerequisites

- Python 3.8+ (for Python utilities)
- Node.js/npm (for MCP servers)
- VS Code (recommended) with extensions from `.vscode/extensions.json`

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/jrb3/tuscaloosa-mortgage-calculator.git
   cd tuscaloosa-mortgage-calculator
   ```

2. **Set up Python environment** (for utility scripts)
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys
   ```

4. **Open in VS Code**
   ```bash
   code tuscaloosa-mortgage-calculator.code-workspace
   ```

### VS Code Features

Once opened in VS Code, you'll have access to:

- **Custom Code Snippets**: Type `mort-` and press Tab for mortgage calculator snippets
  - `mort-input` - Form input field
  - `mort-calc` - Calculation function template
  - `mort-altax` - Alabama property tax calculation
  - `mort-pmi` - PMI calculation logic
  - And 8+ more snippets!

- **Debugging**: Press `F5` to launch Chrome with debugger attached

- **Tasks**: Access via `Ctrl+Shift+P` → "Run Task"
  - Open Mortgage Calculator
  - Run Python scripts
  - Format code

- **Keyboard Shortcuts**:
  - `Ctrl+Shift+L` - Start Live Server
  - `Ctrl+Alt+F` - Format document
  - `F5` - Start debugging

### MCP Servers

This project is configured with three MCP servers for enhanced AI-assisted development:

- **GitHub**: Repository management, PR reviews, issue tracking
- **Filesystem**: Enhanced file operations
- **Context7**: Up-to-date library/framework documentation

To authenticate MCP servers in Claude Code:
```bash
claude
> /mcp
```

## Project Structure

```
tuscaloosa-mortgage-calculator/
├── tuscaloosa-mortgage-calculator.html  # Main calculator application
├── README.md                            # This file
├── LICENSE                              # MIT License
├── CLAUDE.md                            # Claude Code instructions
├── .mcp.json                            # MCP server configuration
├── .env.example                         # Environment variables template
├── requirements.txt                     # Python dependencies
├── .gitignore                           # Git ignore rules
│
├── .vscode/                             # VS Code configuration
│   ├── settings.json                    # Editor settings
│   ├── extensions.json                  # Recommended extensions
│   ├── tasks.json                       # Build/run tasks
│   ├── launch.json                      # Debug configurations
│   ├── keybindings.json                 # Custom shortcuts
│   └── html.code-snippets               # Code snippets
│
├── convert_pdf.py                       # PDF conversion utility
├── r40_russell3000_screen (1).py       # Stock screening script
└── landing-page/                        # Additional web content
```

## How It Works

### Mortgage Payment Formula

Monthly Payment = P × [r(1+r)^n] / [(1+r)^n - 1]

Where:
- P = Principal (loan amount)
- r = Monthly interest rate (annual rate / 12)
- n = Total number of payments (years × 12)

### Alabama Property Tax Calculation

Annual Property Tax = (Appraised Value × 10%) × (Millage Rate / 1000)

Tuscaloosa County uses a 10% assessment rate for residential properties, which is lower than many other states.

### PMI Calculation

PMI is automatically calculated when down payment < 20%:
- Typical rate: 0.5% - 1% of loan amount annually
- This calculator uses 0.5% as the default rate
- PMI can be removed once 20% equity is reached

## Usage Examples

### Example 1: First-Time Homebuyer
- Home Price: $250,000
- Down Payment: $12,500 (5%)
- Interest Rate: 6.5%
- Loan Term: 30 years
- Tax Rate: 46 mills (county median)
- Insurance: $1,200/year

**Result**: Estimated monthly payment including all costs

### Example 2: Custom Millage Rate
If you know your specific property's millage rate:
1. Select "Custom" from the tax rate dropdown
2. Enter your exact millage rate
3. Calculator updates automatically

## Python Utilities

The repository includes additional Python scripts:

### convert_pdf.py
PDF to CSV conversion utility using Docling library.

**Note**: Currently has compatibility issues with Docling API. See [Issues](#known-issues).

### r40_russell3000_screen.py
Russell 3000 stock screening using Rule of 40 metric.

**Usage**:
```bash
source .venv/bin/activate
export FMP_API_KEY="your-api-key"
python "r40_russell3000_screen (1).py" --help
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Known Issues

- `convert_pdf.py`: API compatibility issue with Docling library (line 28)
- Python script filename contains version suffix `(1)` - needs cleanup

## Roadmap

Potential future enhancements:

- [ ] Amortization schedule visualization
- [ ] Comparison mode (multiple scenarios side-by-side)
- [ ] Export results to PDF
- [ ] Save/load calculations (localStorage)
- [ ] Dark mode support
- [ ] Progressive Web App (PWA) features for offline use
- [ ] Additional Alabama county support

## Browser Compatibility

Tested and working on:
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Technical Details

- **No Build Process**: Pure HTML/CSS/JavaScript - no compilation required
- **No External Dependencies**: All code is self-contained in one file
- **Client-Side Only**: All calculations happen in the browser
- **Privacy-Focused**: No data is sent to external servers

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Alabama property tax rates sourced from Tuscaloosa County Revenue Commissioner
- Mortgage calculation formulas based on standard amortization tables
- Built with Claude Code for enhanced AI-assisted development

## Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/jrb3/tuscaloosa-mortgage-calculator/issues) page
2. Review [CLAUDE.md](CLAUDE.md) for development guidance
3. Open a new issue with detailed information

## Author

**jrbarrow3**
- GitHub: [@jrb3](https://github.com/jrb3)

---

**Disclaimer**: This calculator provides estimates only. Actual mortgage payments may vary. Consult with a licensed mortgage professional for accurate quotes and financial advice.
