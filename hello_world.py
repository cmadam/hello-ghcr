import argparse
import json
import logging
import os
import sys
import time

"""A simple logger that prints 120 times a message every 5 seconds."""


# start_command:
#   "/app/bootstrap_sdk.sh
#      --fileset-location {{ bindings.input_artifact_path.binding.path }}
#      --model-location {{ bindings.model_to_use.binding.path }}
#      --output-custom-path {{ bindings.custom.binding.path }}
#      --blah blah


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
        "--output-custom-path",
        type=str,
        required=False,
        help="The name of the output path used by this build",
    )
    args = parser.parse_args()

    logging.info("The fileset used by this build is located at %s", args.fileset_location)
    logging.info("The model used by this build is located at %s", args.model_location)
    logging.info("The output folder of this build is at %s", args.output_custom_path)

    output_path = args.output_custom_path
    assert isinstance(output_path, str) and output_path, "Invalid output path"
    os.makedirs(name=output_path, exist_ok=True)

    for i in range(120):
        logging.info("Example demonstrating how to bring your own image in a workflow.")
        time.sleep(0.5)
        if i % 10 == 0:
            file_path = os.path.join(output_path, f"artifact_{i}.txt")
            with open(file_path, "w") as fp:
                fp.write(f"This is artifact {i}\n")
    logging.info("LLMB_ARTIFACT_ID:%s LLMB_ARTIFACT_PATH:%s", "output_1", output_path)
