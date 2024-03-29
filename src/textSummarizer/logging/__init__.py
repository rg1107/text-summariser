import os
import sys
import logging

import os
import sys
import logging

# Initialising the pattern of a single log file and the file destination where the logs will be written
logging_pattern = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

# Initialising the config for the logging module, allowing the logs to be printed on the file as well as stdout using
# FileHandler and StreamHandler respectively
logging.basicConfig(
    level=logging.INFO,
    format=logging_pattern,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# Giving custom name to the logger
logger = logging.getLogger("textSummarizerLogger")
