# Use an Nvidia base image
FROM nvcr.io/nvidia/cuda:12.8.0-cudnn-runtime-ubi9

# Create app directory with proper ownership
RUN mkdir -p /app && \
    chown -R 1000:1000 /app

WORKDIR /app

# Copy with ownership
COPY --chown=1000:1000 hello_world.py .

# Switch to non-root user
USER 1000

CMD ["python", "hello_world.py"]
