import os
from datetime import datetime


# Base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Log directory
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Log file path (daily log)
LOG_FILE = os.path.join(LOG_DIR, f"log_{datetime.now().date()}.txt")

# Silent mode flag (default False, overridden by CLI args)
SILENT_MODE = False

# === Configurable Settings ===
FLUSH_INTERVAL = 10  # Time in seconds between log flushes (buffer write)