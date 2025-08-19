#!/bin/bash

chmod +x open_reports.sh

echo "Opening HTML report"
open html-report/index.html
#
#echo "Opening Allure results"
#allure serve allure-results

echo "Opening Allure reports"
allure serve allure-report