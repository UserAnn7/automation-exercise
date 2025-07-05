#!/bin/bash
set -e

echo "Making run_tests executable"
chmod +x run_tests.sh

echo "Cleaning old reports..."
rm -rf allure-results allure-report screenshots report.html

echo "Running tests with pytest..."
poetry run pytest --html=report.html --self-contained-html --alluredir=allure-results

echo "Generating Allure report..."
allure generate allure-results -o allure-report --clean

echo "Allure report available at: ./allure-report/index.html"