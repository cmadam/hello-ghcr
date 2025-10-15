import time
import logging

"""A simple logger that prints 1000 times a message every 5 seconds."""

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

if __name__ == "__main__":
    for i in range(1000):
        logging.info("Example demonstrating how to bring your own image in a workflow.")
        time.sleep(5)
