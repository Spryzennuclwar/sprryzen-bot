# agent/actions.py
# Safe whitelisted automation actions using pyautogui.
# NOTE: pyautogui will control the local machine; test carefully.

import time
import pyautogui

def open_notepad():
    """Windows example: uses start menu typing. Non-Windows may fail."""
    pyautogui.press('win')
    time.sleep(0.6)
    pyautogui.write('notepad')
    pyautogui.press('enter')
    return "opened notepad"

def type_text(text: str, interval: float = 0.01):
    """Type text where the cursor is focused."""
    pyautogui.write(text, interval=interval)
    return f"typed {len(text)} chars"

def press_key(key: str):
    """Press a single key (e.g., 'enter', 'tab')."""
    pyautogui.press(key)
    return f"pressed {key}"

# WHITELIST maps public command names (strings) to function objects
WHITELIST = {
    "open_notepad": open_notepad,
    "type_text": type_text,
    "press_key": press_key,
}
