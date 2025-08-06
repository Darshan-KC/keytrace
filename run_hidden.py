import subprocess
import sys
import os
import platform

def run_in_background():
    system = platform.system()
    script_path = os.path.join(os.path.dirname(__file__), "main.py")
    base_cmd = [sys.executable, script_path, "--silent"]
    pass