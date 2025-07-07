# Automation Exercise

This project contains automated tests for the following test cases from automationexercise.com:

🔹 API Tests 

1. Update user information
(PUT request to update user account details)

Test Case Reference → https://automationexercise.com/api_list#collapse13

2. Search product without search product parameter (Negative test)
(GET request without search_product parameter — validates error handling)

Test Case Reference → https://automationexercise.com/api_list#collapse6

🔹 UI Test

Place Order: Register before Checkout
(Full end-to-end user flow including registration, adding product to cart, placing an order, and deleting account)

Test Case Reference → https://automationexercise.com/test_cases#collapse15

# Setup and Test Execution Guide

This guide provides instructions for setting up, running automated tests, generating reports using Docker and Allure.

## Prerequisites

- Docker Desktop app
- Allure installed

## Setup Instructions

### 1. Make Scripts Executable

Run the following commands in your console to make the scripts executable:

```bash
chmod +x run_tests.sh
chmod +x open_reports.sh
chmod +x install.sh
```

### 2. Build Docker Container

Build and start the Docker container with:

```bash
docker compose up --build -d
```

### 3. Execute Tests

Run the automated tests inside the Docker container:

```bash
docker exec -it automation-tests ./run_tests.sh
```

### 4. Open Reports

To view the test reports, execute:

```bash
./open_reports.sh
```

## Stopping and Cleaning Up

### 5. Stop the Container

To stop the container without removing it:

```bash
docker compose stop
```

### 6. Shut Down and Clean Container

To shut down and remove the container:

```bash
docker compose down
```

## Alternative: Local Installation

If you prefer a local installation instead of using Docker, run the following commands:

```bash
./install.sh
./run_tests.sh
./open_reports.sh
```
If you choose to run tests locally (using a local Playwright installation), make sure to uncomment the following fixtures in your conftest.py file:

```
# Uncomment these fixtures for local browser testing
@pytest.fixture(scope="function")
def browser(request):
    ...

@pytest.fixture(scope="function")
def page(browser, request):
    ...
```