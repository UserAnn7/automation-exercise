echo "Cleaning old reports and har logs..."
rm -rf allure-results allure-report html-report screenshots_for_failed_cases logs har

echo "Running tests with pytest..."
poetry run behave