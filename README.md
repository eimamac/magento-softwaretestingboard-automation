# POM-Based Playwright Test Suite

This repository contains a sample test automation framework using [Playwright](https://playwright.dev/) and Python’s [pytest](https://docs.pytest.org/) test runner. The framework follows the Page Object Model (POM) design pattern for clean, maintainable, and scalable test code.

## Features
- **Page Object Model (POM):** Encapsulates page locators and actions within dedicated classes for easier maintenance.
- **Playwright for Browser Automation:** Fast and reliable testing across multiple browsers.
- **pytest for Test Execution:** Simple and extensible test runner with fixtures and clear reports.

## Requirements
- Python 3.9+ (or the latest Python version)
- [pip](https://pypi.org/project/pip/) for package management

## Installation
1. **Clone this repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   python -m venv venv
   ```


### On Linux/MacOS:
```bash
source venv/bin/activate.
   ```
### On Windows:
```bash
venv\Scripts\activate
   ```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
   ```

## Running Tests
```bash
python -m pytest tests/test_buy_flow.py
   ```
