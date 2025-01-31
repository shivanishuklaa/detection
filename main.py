import os
import logging
import subprocess

# Configure Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Define paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")

# Helper function to run scripts
def run_script(script_name):
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    logging.info(f"Running {script_name}...")
    result = subprocess.run(["python", script_path], capture_output=True, text=True)

    if result.returncode == 0:
        logging.info(f"{script_name} completed successfully.\n")
    else:
        logging.error(f"Error in {script_name}:\n{result.stderr}")
        exit(1)

# Run Pipeline
if __name__ == "__main__":
    logging.info("Starting Steel Defect Detection Pipeline...")

    try:
        # Step 1: Preprocess the data
        run_script("preprocess.py")

        # Step 2: Train the model
        run_script("train.py")

        # Step 3: Perform inference on test images
        run_script("infer.py")

        logging.info("Pipeline execution completed successfully!")

    except Exception as e:
        logging.error(f"Pipeline failed: {str(e)}")
        exit(1)