FROM ubuntu:latest
# Select Ubuntu as the base image.

WORKDIR /app
# Set /app as the working directory.

COPY . /app
# Copy application files into the image.

RUN apt-get update && apt-get install -y python3 python3-pip
# Install Python and pip.

ENV NAME World
# Set the environment variable.

CMD ["python3", "app.py"]
# Start the Python application when the container runs.