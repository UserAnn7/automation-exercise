# Automation Exercise

This guide provides instructions for setting up and running automated tests using Docker and Allure.

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
