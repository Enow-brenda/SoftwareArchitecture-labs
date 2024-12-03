# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8002 for the user service
EXPOSE 8002

# Define environment variable for FastAPI
ENV UVICORN_CMD="uvicorn user_service:app --host 0.0.0.0 --port 8002"

# Run the FastAPI app
CMD ["sh", "-c", "$UVICORN_CMD"]

