# Use a base image with python and necessary libraries installed
FROM python:3.8-slim-buster

# Update package list and install tkinter dependencies
RUN apt-get update && apt-get install -y \
    python3-tk \
    tk-dev \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt /

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Set the working directory in the container to /app
WORKDIR /app

# Set the Flask application environment variable
ENV FLASK_APP=app.py

# Set the DISPLAY environment variable to use the host's X server
ENV DISPLAY=host.docker.internal:0.0

# Run the command to start the server
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
