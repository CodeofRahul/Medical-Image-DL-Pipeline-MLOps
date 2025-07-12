import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifierLogger")

__all__ = ['logger']    # Expose the logger to other modules



# The line __all__ = ['logger'] in a Python module defines the list of public objects that will be imported when a user imports the module using the syntax from module import *.

# In short, it means that if someone does from cnnClassifier.logger import *, only the logger object will be imported from this module.
