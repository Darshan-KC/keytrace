import subprocess
import sys
import os
import signal
import time

MAIN_PATH = os.path.join(os.path.dirname(__file__), "..", "main.py")

def test_main_silent_mode_launch():
    proc = subprocess.Popen(
        [sys.executable, MAIN_PATH, "--silent"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    time.sleep(2)
    proc.terminate()
    try:
        proc.wait(timeout=2)
    except subprocess.TimeoutExpired:
        proc.kill()
    assert proc.returncode == 0 or proc.returncode is None
