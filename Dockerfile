# Use python slim base image (v 0.0.23)
FROM python:3.12-slim

# Use an Nvidia base image (v 0.0.20)
#FROM nvcr.io/nvidia/cuda:12.8.0-cudnn-runtime-ubi9

# Create app directory
RUN mkdir -p /app

WORKDIR /app

# Copy app files
COPY hello_world.py .

CMD ["python", "hello_world.py"]
