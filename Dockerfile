# Use a minimal Python base image
FROM python:3.12-slim

WORKDIR /app
COPY hello_world.py .
COPY bootstrap_sdk.sh .

CMD ["python", "hello_world.py"]
