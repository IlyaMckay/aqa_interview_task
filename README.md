# AccuWeather BDD Test Project

This project uses Python + Playwright + Behave + Allure for testing AccuWeather.com

## Installation

```bash
pip install -r requirements.txt
playwright install
```

## Run tests and reports

```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/firefox features/

allure serve reports/firefox
allure generate reports/firefox -o allure-report --clean
```
