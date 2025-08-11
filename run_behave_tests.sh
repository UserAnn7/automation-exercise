echo "Cleaning old reports and har logs..."
rm -rf allure-results allure-report html-report screenshots_for_failed_cases logs har

echo "Running tests with behave..."
poetry run behave -f allure_behave.formatter:AllureFormatter -o allure-report