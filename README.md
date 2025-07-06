## Precondition: Have Docket Desktop app

## 1. Build docker container
```
docker compose up --build -d
```
## 2. Execute tests
```
docker exec -it automation-tests ./run_tests.sh
```
## 3. To stop the container without cleening it

```
docker compose stop
```
## 4. To shut down and cleen container

```
docker compose down
```
