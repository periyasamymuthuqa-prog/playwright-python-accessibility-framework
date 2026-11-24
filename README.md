# Playwright Python Accessibility & UI Automation Framework

A modular test automation framework built with **Python**, **Playwright**, **Pytest**, and **Axe-core** demonstrating UI automation, automated WCAG 2.1 compliance scanning, SQL database verification, and GitHub Actions CI/CD integration.

## Tech Stack
- **Language:** Python 3.11+
- **Browser Automation:** Playwright (`pytest-playwright`)
- **Accessibility Engine:** Axe-core (`axe-playwright-python`)
- **Test Runner & Reporting:** Pytest & `pytest-html`
- **Database Verification:** SQL (`sqlite3`)
- **CI/CD:** GitHub Actions

## Project Structure
```text
├── .github/workflows/playwright.yml   # CI/CD pipeline
├── pages/login_page.py                # Page Object Model (POM)
├── tests/
│   ├── test_login_ui.py               # Functional UI smoke tests
│   ├── test_accessibility.py          # WCAG 2.1 Axe-core audit
│   └── test_db_validation.py          # SQL database verification
├── conftest.py                        # Pytest fixtures
├── pytest.ini                         # Pytest configuration & HTML reporting
└── requirements.txt                   # Python dependencies
```

## Setup & Execution
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```
2. **Run all tests:**
   ```bash
   pytest
   ```
3. **Run only Accessibility (WCAG) tests:**
   ```bash
   pytest -m a11y
   ```
