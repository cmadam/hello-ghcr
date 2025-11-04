import argparse
import logging
import os
import sys
import time

"""A simple logger that prints 120 times a message every 5 seconds."""


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sample app")
    parser.add_argument(
        "--fileset-location",
        type=str,
        required=False,
        help="The name of the fileset used by this build",
    )
    parser.add_argument(
        "--model-location",
        type=str,
        required=False,
        help="The name of the model used by this build",
    )
    parser.add_argument(
        "--output-path",
        type=str,
        required=False,
        help="The name of the output path used by this build",
    )
    parser.add_argument(
        "--simulate-failure",
        action="store_true",
        required=False,
        help="Simulate a failure",
    )

    args = parser.parse_args()
    normal_run: bool = args.simulate_failure is None
    logging.info("The fileset used by this build is located at %s", args.fileset_location)
    logging.info("The model used by this build is located at %s", args.model_location)
    logging.info("The output folder of this build is at %s", args.output_path)

    output_path = args.output_path
    assert isinstance(output_path, str) and output_path, "Invalid output path"
    os.makedirs(name=output_path, exist_ok=True)

    num_iterations = int(os.getenv("NUMBER_OF_ITERATIONS", "120"))
    sleep_interval = float(os.getenv("SLEEP_INTERVAL", "0.5"))
    logging.info("Iterating %d times; sleep interval = %f seconds", num_iterations, sleep_interval)

    for i in range(num_iterations):
        logging.info("Example demonstrating how to bring your own image in a workflow.")
        time.sleep(sleep_interval)
        if i % 10 == 0 and normal_run:
            file_path = os.path.join(output_path, f"artifact_{i}.txt")
            with open(file_path, "w") as fp:
                fp.write(f"This is artifact {i}\n")
    if normal_run:
        logging.info("LLMB_ARTIFACT_ID:%s LLMB_ARTIFACT_PATH:%s", "output_1", output_path)
    else:
        logging.error("A simulated error occurred")
        sys.exit(1)
