# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN apt-get update && \
    apt-get install -y --no-install-recommends libgl1-mesa-glx && \
    pip3 install --no-cache-dir -r requirements.txt && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Package the YOLOv5 model
RUN tar -czvf model.tar.gz yolov5s.pt

# Set environment variables
ENV AWS_DEFAULT_REGION=us-west-2

# Install the AWS CLI
RUN apt-get update && \
    apt-get install -y --no-install-recommends awscli && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Run the create SageMaker endpoint script
CMD ["python3", "create_sagemaker_endpoint.py"]
