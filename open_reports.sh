#!/bin/bash

chmod +x open_reports.sh

echo "Opening HTML report"
open report.html

echo "Opening Allure results"
allure serve allure-results