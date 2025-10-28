# Use a minimal Python base image
FROM python:3.12-slim

WORKDIR /app1
COPY hello_world.py .

CMD ["python", "hello_world.py"]
