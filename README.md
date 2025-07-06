## Precondition: Have Docket Desktop app and Allure installed
## 1. Enter the next command in console
```
chmod +x run_tests.sh
chmod +x open_reports.sh
chmod +x intall.sh
```
## 2. Build docker container
```
docker compose up --build -d
```
## 3. Execute tests
```
docker exec -it automation-tests ./run_tests.sh
```
## 4. Open reports
```
./open_reports.sh
```

## 5. To stop the container without cleening it

```
docker compose stop
```
## 6. To shut down and cleen container

```
docker compose down
```

# You may choose local installation instead of Docker installation
```
./intall.sh
./run_tests.sh
./open_reports.sh
```
