# docker login # this is to login to docker hub
# docker build -t smart-job-navigator .
# docker tag smart-job-navigator yavuz53/smart-job-navigator:latest
# push yavuz53/smart-job-navigator:latest

LABEL maintainer="Yavuz Kulaber <yavuzkulaber53@hotmail.com>" \
      description="Docker image for Smart Job Navigator" \
      label="1.0"

# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Gradio will run on
EXPOSE 7860

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Command to run the application
CMD ["python", "smart_job_navigator/gradio_app.py"]
