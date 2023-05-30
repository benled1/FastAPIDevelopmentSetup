# Getting Started Developing in FastAPI

## Setting up your environment.
To avoid environment conflicts we will use docker to run our application locally. To get started with the environment, there is a docker compose file included in this repository that is able to run a FastAPI application alongside a PostgreSQL database. The docker compose container will run the main.py file as the FastAPI backend. This can be changed by editing the ```command: uvicorn main:app --host 0.0.0.0 --port 8000``` in the compose file.

### 
