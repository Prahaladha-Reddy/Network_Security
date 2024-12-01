import logging
import os
from datetime import datetime

# Construct the log file path relative to the "Network_Security" folder
log_folder = os.path.join(os.path.dirname(__file__), "logs")
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

logs_path = os.path.join(log_folder, "network_security.log")

LOG_FILE = f"[{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}].log"
logs_path = os.path.join(logs_path, LOG_FILE)

os.makedirs(os.path.dirname(logs_path), exist_ok=True)

logging.basicConfig(
    filename=logs_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s: %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)