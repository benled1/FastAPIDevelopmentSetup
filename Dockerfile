FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Copy current directory to the container
COPY . .

# Install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Everything else is handled in the docker compose file.