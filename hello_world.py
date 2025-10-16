import json
import time
import logging

"""A simple logger that prints 120 times a message every 5 seconds."""

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

if __name__ == "__main__":
    for i in range(120):
        logging.info("Example demonstrating how to bring your own image in a workflow.")
        time.sleep(5)
        if i % 10 == 0:
            filename = f"artifact_{i}.txt"
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
