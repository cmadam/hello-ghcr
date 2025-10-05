import time
import logging

"""A simple infinite logger that prints “Hello World” every 5 seconds."""

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

if __name__ == "__main__":
    while True:
        logging.info("Hello World")
        time.sleep(5)
