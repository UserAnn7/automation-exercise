#!/bin/bash

echo "Cleaning old reports..."
rm -rf allure-results allure-report screenshots report.html

echo "Running tests with pytest..."
poetry run pytest -s --soft-asserts --html=report.html --self-contained-html --alluredir=allure-results

#echo "Generating Allure report..."
#allure generate allure-results -o allure-report --clean

echo "Opening HTML report"
open report.html

echo "Opening Allure results"
allure serve allure-results