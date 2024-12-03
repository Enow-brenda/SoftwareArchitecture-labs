# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /function

# Install system dependencies for image processing
RUN apt-get update && apt-get install -y \
    wget \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install OpenFaaS watchdog
RUN wget https://github.com/openfaas/classic-watchdog/releases/download/0.3.1/fwatchdog-amd64 \
    && chmod +x fwatchdog-amd64 \
    && mv fwatchdog-amd64 /usr/bin/

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the function handler
COPY handler.py .

# Set environment variables for the function
ENV fprocess="python3 handler.py"
EXPOSE 8080

# Use OpenFaaS watchdog as the entrypoint
ENTRYPOINT ["/usr/bin/fwatchdog-amd64"]



