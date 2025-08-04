#!/bin/bash

set -e  # Exit immediately if any command fails

echo "Cleaning old reports..."
rm -rf allure-results allure-report html-report screenshots_for_failed_cases logs har

echo "Running tests with pytest..."
poetry run pytest -s --soft-asserts \
  --html=html-report/index.html --self-contained-html \
  --alluredir=allure-results

echo "Generating Allure report..."
allure generate allure-results -o allure-report --clean

echo "Done. Reports generated:"
echo "- HTML Report: html-report/index.html"
echo "- Allure Report: allure-report/"