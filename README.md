## Precondition: Have Docket Desktop app and Allure installed
## Enter the next command in console
```
chmod +x run_tests.sh && chmod +x open_reports.sh
```
## 1. Build docker container
```
docker compose up --build -d
```
## 2. Execute tests
```
docker exec -it automation-tests ./run_tests.sh
```
## 3. Open reports
```
./open_reports.sh
```

## 4. To stop the container without cleening it

```
docker compose stop
```
## 5. To shut down and cleen container

```
docker compose down
```
