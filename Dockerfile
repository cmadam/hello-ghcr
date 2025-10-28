# Use a minimal Python base image
FROM nvidia/cuda:12.8.0-cudnn-runtime-ubi9

WORKDIR /app1
COPY hello_world.py .

CMD ["python", "hello_world.py"]
