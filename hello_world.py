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
        required=True,
        help="The name of the fileset used by this build",
    )
    parser.add_argument(
        "--model-location",
        type=str,
        required=True,
        help="The name of the model used by this build",
    )
    parser.add_argument(
        "--output-custom-path",
        type=str,
        required=True,
        help="The name of the output path used by this build",
    )
    args = parser.parse_args()

    logging.info("The fileset used by this build is located at %s", args.fileset_location)
    logging.info("The model used by this build is located at %s", args.model_location)
    logging.info("The output folder of this build is at %s", args.output_custom_path)

    for i in range(120):
        logging.info("Example demonstrating how to bring your own image in a workflow.")
        time.sleep(5)
        if i % 10 == 0:
            filename = os.path.join(args.output_custom_path, f"artifact_{i}.txt")
            with open(filename, "w") as fp:
                fp.write(f"This is artifact {i}\n")
            dct = {
                "gb_step_id": "67a3bfcd-cbc6-49fe-908c-f52ea5f7242e",
                "gb_build_id": "0abd12c2-c89f-4681-8477-5499d50d37cf",
                "gb_step_name": "merge_model",
                "gb_progress": {"progress": 0},
                "gb_status": "running",
                "gb_data_ready": {filename: "path"},
                "gb_new_artifact": {"path": filename}
            }
            logging.info(json.dumps(dct))
