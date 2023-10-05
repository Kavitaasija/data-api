A simple repository for DevOps Journey
======================================

# Devops-journey

This is a FastAPI project that demonstrates a simple API.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Local Development](#local-development)
    - [Setting up Python Virtual Environment](#setting-up-python-virtual-environment)
    - [Install all the requirements](#install-all-the-requirements)
    - [Run the HTTP server locally](#run-the-http-server-locally)
- [Dockerization](#dockerization)
    - [Build the docker image](#build-the-docker-image)
    - [Run the docker image as a container](#run-the-docker-image-as-a-container)

## Prerequisites

Before getting started, make sure you have the following prerequisites installed on your system:

- Python 3.9 or higher
- Docker (if you want to run the application in a container)

## Local Development

### Setting up Python Virtual Environment

It's a good practice to use a Python virtual environment to isolate your project's dependencies. To create and activate a virtual environment, follow these steps:

```shell
# Create a virtual environment (replace 'myenv' with your preferred name)
python -m venv myenv

# Activate the virtual environment
# On Windows:
myenv\Scripts\activate
# On macOS and Linux:
source myenv/bin/activate
```

## How to run the project locally

### Install all the requirements

```shell
pip install -m requirements.txt
```

### Run the HTTP server locally

```shell
uvicorn main:app --port 8081 --reload
```

### Build the docker image

```shell
docker build -t python-api-app .
```

### Run the docker image as a container

```shell
docker run -p 8081:8081 python-api-app
```

#### Deactivate the virtual environment

```shell
deactivate
```
