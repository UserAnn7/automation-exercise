#!/bin/bash

echo "Cleaning old reports..."
rm -rf allure-results allure-report screenshots logs report.html

echo "Running tests with pytest..."
poetry run pytest -s --soft-asserts --html=report.html --self-contained-html --alluredir=allure-results

#echo "Generating Allure report..."
#allure generate allure-results -o allure-report --clean