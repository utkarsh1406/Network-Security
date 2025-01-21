import logging
import os
from datetime import datetime

# Define log file name based on the current date and time
LOG_File = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

# Define the log path
log_path = os.path.join(os.getcwd(), "logs")

# Create the logs directory if it doesn't exist
os.makedirs(log_path, exist_ok=True)

# Full log file path
Log_File_Path = os.path.join(log_path, LOG_File)

# Configure logging
logging.basicConfig(
    filename=Log_File_Path,
    format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Example usage of logging
logging.info("Logging has been set up successfully.")
