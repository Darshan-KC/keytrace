import os
from datetime import datetime

# Create logs directory if not present
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# File path with date
LOG_FILE = os.path.join(LOG_DIR, f"log_{datetime.now().date()}.txt")