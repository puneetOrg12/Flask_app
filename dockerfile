# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9-slim

# Allow statements and log messages to be output immediately
ENV PYTHONUNBUFFERED True

# Set the working directory
WORKDIR /app

# Install the dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY . .

# Run the application
CMD ["python", "app.py"]

