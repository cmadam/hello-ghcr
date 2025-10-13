# Use a minimal Python base image
FROM python:3.11-slim

WORKDIR /app
COPY app.py .
COPY bootstrap_sdk.sh .

CMD ["python", "app.py"]
