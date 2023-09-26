A simple repository for DevOps Journey
======================================

## How to run the project locally

## Install all the requirements

```shell
pip install -m requirements.txt
```

## Run the HTTP server locally for testing/debugging

```shell
uvicorn main:app --port 8080 --reload
```

## Build the docker image

```shell
docker build -t data-api .
```

## Run the docker image as a container

```shell
docker run -p 8080:8080 data-api
```

### Deactivate the virtual environment

```shell
deactivate
```
