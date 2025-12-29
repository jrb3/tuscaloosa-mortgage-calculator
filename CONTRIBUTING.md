# Contributing to Tuscaloosa County Mortgage Calculator

Thank you for considering contributing to this project! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Branch Naming Conventions](#branch-naming-conventions)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Pull Request Process](#pull-request-process)
- [Code Style Guide](#code-style-guide)
- [Testing Guidelines](#testing-guidelines)
- [Documentation Standards](#documentation-standards)

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors. Please be respectful and constructive in all interactions.

### Expected Behavior

- Use welcoming and inclusive language
- Be respectful of differing viewpoints and experiences
- Gracefully accept constructive criticism
- Focus on what is best for the community
- Show empathy towards other community members

## Getting Started

### Prerequisites

- Git
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Python 3.8+ (for utility scripts)
- VS Code (recommended)
- Node.js/npm (for MCP servers)

### Setup

1. **Fork the repository** on GitHub

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR-USERNAME/tuscaloosa-mortgage-calculator.git
   cd tuscaloosa-mortgage-calculator
   ```

3. **Add upstream remote**
   ```bash
   git remote add upstream https://github.com/jrb3/tuscaloosa-mortgage-calculator.git
   ```

4. **Set up Python environment** (optional, for Python scripts)
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

5. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys if needed
   ```

6. **Open in VS Code**
   ```bash
   code tuscaloosa-mortgage-calculator.code-workspace
   ```

## Development Workflow

### 1. Create a Feature Branch

Always create a new branch for your work:

```bash
git checkout main
git pull upstream main
git checkout -b feature/your-feature-name
```

### 2. Make Your Changes

- Write clean, readable code
- Follow the code style guide (see below)
- Add comments where necessary
- Test your changes thoroughly

### 3. Test Locally

- Open `tuscaloosa-mortgage-calculator.html` in multiple browsers
- Test all input combinations
- Verify calculations are accurate
- Check responsive design on mobile

### 4. Commit Your Changes

Follow the commit message guidelines (see below):

```bash
git add .
git commit -m "Add feature: brief description"
```

### 5. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 6. Create a Pull Request

Go to GitHub and create a pull request from your fork to the main repository.

## Branch Naming Conventions

Use descriptive branch names following these patterns:

### Feature Branches
```
feature/add-amortization-schedule
feature/dark-mode-support
feature/export-to-pdf
```

### Bug Fix Branches
```
bugfix/fix-pmi-calculation
bugfix/mobile-layout-issue
bugfix/tax-rate-validation
```

### Enhancement Branches
```
enhancement/improve-ui-accessibility
enhancement/optimize-calculations
enhancement/add-input-tooltips
```

### Documentation Branches
```
docs/update-readme
docs/add-api-documentation
docs/improve-code-comments
```

### Refactoring Branches
```
refactor/extract-calculation-logic
refactor/modularize-javascript
refactor/improve-css-organization
```

## Commit Message Guidelines

### Format

```
<type>: <subject>

<body (optional)>

<footer (optional)>
```

### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code formatting (no functional changes)
- **refactor**: Code refactoring
- **test**: Adding or updating tests
- **chore**: Maintenance tasks (dependencies, build config)

### Examples

**Good commit messages:**
```
feat: Add amortization schedule visualization

Implements a detailed amortization schedule showing payment breakdown
for each month of the loan term. Includes principal, interest, and
remaining balance calculations.

Closes #42
```

```
fix: Correct PMI calculation for LTV > 95%

PMI rate was incorrectly using 0.5% for all LTV ratios. Updated to use
tiered rates: 0.5% for 80-95% LTV, 1.0% for >95% LTV.

Fixes #38
```

```
docs: Update README with deployment instructions
```

**Bad commit messages:**
```
fixed stuff
updated code
changes
wip
```

### Rules

1. Use imperative mood ("Add feature" not "Added feature")
2. First line should be ≤ 50 characters
3. Capitalize first letter
4. No period at the end of subject line
5. Separate subject from body with blank line
6. Body should explain *what* and *why*, not *how*
7. Reference issues and PRs in footer

## Pull Request Process

### Before Submitting

- [ ] Code follows the style guidelines
- [ ] Self-review of your code completed
- [ ] Comments added for complex logic
- [ ] Documentation updated (if needed)
- [ ] No console.log() or debug code left behind
- [ ] Tested on multiple browsers
- [ ] Mobile responsiveness verified

### PR Title Format

Use the same format as commit messages:

```
feat: Add dark mode toggle
fix: Resolve mobile layout overflow issue
docs: Improve installation instructions
```

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix (non-breaking change fixing an issue)
- [ ] New feature (non-breaking change adding functionality)
- [ ] Breaking change (fix or feature causing existing functionality to break)
- [ ] Documentation update

## How Has This Been Tested?
Describe the tests you ran and browsers tested

## Screenshots (if applicable)
Add screenshots for UI changes

## Checklist
- [ ] My code follows the style guidelines
- [ ] I have performed a self-review
- [ ] I have commented complex code
- [ ] My changes generate no new warnings
- [ ] I have tested on multiple browsers
```

### Review Process

1. A maintainer will review your PR within 3-5 business days
2. Address any requested changes
3. Once approved, a maintainer will merge your PR
4. Your contribution will be included in the next release!

## Code Style Guide

### HTML

- Use semantic HTML5 elements
- Proper indentation (2 spaces)
- Include ARIA attributes for accessibility
- Use meaningful class and ID names

```html
<!-- Good -->
<section class="calculator-container" aria-label="Mortgage Calculator">
  <div class="form-group">
    <label for="homePrice">Home Price:</label>
    <input type="number" id="homePrice" name="homePrice" aria-required="true">
  </div>
</section>

<!-- Bad -->
<div class="cont">
  <div class="grp">
    <label>Price</label>
    <input type="number">
  </div>
</div>
```

### CSS

- Use meaningful class names (BEM methodology preferred)
- Group related styles together
- Mobile-first responsive design
- Avoid !important unless absolutely necessary
- Use CSS variables for repeated values

```css
/* Good */
:root {
  --primary-color: #4CAF50;
  --border-radius: 5px;
}

.calculator-container {
  background-color: white;
  border-radius: var(--border-radius);
  padding: 30px;
}

.calculator-container__header {
  color: #333;
  text-align: center;
}

/* Bad */
.cont {
  background: white !important;
  border-radius: 5px;
}

.hdr {
  color: #333;
}
```

### JavaScript

- Use ES6+ features where appropriate
- Camel case for variables and functions
- Pascal case for constructors/classes
- Constants in UPPERCASE
- Add JSDoc comments for functions
- Handle errors gracefully

```javascript
// Good
/**
 * Calculates monthly mortgage payment
 * @param {number} principal - Loan amount
 * @param {number} annualRate - Annual interest rate (percentage)
 * @param {number} years - Loan term in years
 * @returns {number} Monthly payment amount
 */
function calculateMonthlyPayment(principal, annualRate, years) {
  try {
    const monthlyRate = annualRate / 12 / 100;
    const numberOfPayments = years * 12;

    if (monthlyRate === 0) {
      return principal / numberOfPayments;
    }

    return principal *
      (monthlyRate * Math.pow(1 + monthlyRate, numberOfPayments)) /
      (Math.pow(1 + monthlyRate, numberOfPayments) - 1);
  } catch (error) {
    console.error('Error calculating payment:', error);
    return 0;
  }
}

// Bad
function calc(p, r, y) {
  var mr = r / 12 / 100;
  var n = y * 12;
  return p * (mr * Math.pow(1 + mr, n)) / (Math.pow(1 + mr, n) - 1);
}
```

### Python

- Follow PEP 8 style guide
- Use Black formatter (configured in VS Code)
- Type hints for function signatures
- Docstrings for all functions/classes
- Maximum line length: 88 characters

```python
# Good
from typing import Optional

def calculate_property_tax(
    home_value: float,
    millage_rate: float,
    assessment_rate: float = 0.10
) -> float:
    """
    Calculate annual property tax for Alabama properties.

    Args:
        home_value: Appraised home value in dollars
        millage_rate: Local millage rate (mills)
        assessment_rate: Assessment rate (default 10% for residential)

    Returns:
        Annual property tax amount
    """
    assessed_value = home_value * assessment_rate
    return assessed_value * (millage_rate / 1000)

# Bad
def calc_tax(val, rate):
    return val * 0.1 * (rate / 1000)
```

## Testing Guidelines

### Manual Testing Checklist

When making changes, test:

- [ ] All calculations are mathematically correct
- [ ] Form validation works properly
- [ ] Invalid inputs are handled gracefully
- [ ] Mobile responsive design (test at 320px, 768px, 1024px)
- [ ] Browser compatibility (Chrome, Firefox, Safari, Edge)
- [ ] Keyboard navigation works
- [ ] Screen reader accessibility

### Test Cases for Calculations

Verify these scenarios:

1. **Standard mortgage**: $250,000, 20% down, 6.5%, 30 years
2. **Zero interest**: Any principal, 0% rate
3. **High LTV**: < 20% down payment (PMI should apply)
4. **Edge cases**: $0 values, maximum values, decimal inputs
5. **All tax rates**: County average, median, city, custom

### Adding Automated Tests (Future)

When adding tests:

- Place test files in `tests/` directory
- Name test files `test_*.js` or `test_*.py`
- Use descriptive test names
- Test both success and failure cases
- Aim for >80% code coverage

## Documentation Standards

### Code Comments

- Explain *why*, not *what* (code should be self-explanatory)
- Update comments when code changes
- Use JSDoc for JavaScript functions
- Keep comments concise and clear

```javascript
// Good
// PMI is required when LTV exceeds 80% per lending standards
if (ltvRatio > 80) {
  monthlyPMI = calculatePMI(loanAmount);
}

// Bad
// Check if ltvRatio is greater than 80
if (ltvRatio > 80) {
  monthlyPMI = calculatePMI(loanAmount);
}
```

### Documentation Files

- **README.md**: User-facing documentation
- **CLAUDE.md**: Development guidelines for AI-assisted coding
- **CONTRIBUTING.md**: This file
- Add inline documentation for complex algorithms
- Update docs when functionality changes

## Questions?

If you have questions:

1. Check existing [Issues](https://github.com/jrb3/tuscaloosa-mortgage-calculator/issues)
2. Review [CLAUDE.md](CLAUDE.md) for development setup
3. Open a new issue with the `question` label

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing! 🎉
