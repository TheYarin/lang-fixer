from time import sleep
from pynput import keyboard
from pynput.keyboard import KeyCode

def on_press(key: KeyCode):
    try:
        key_code = key.vk
    except AttributeError:
        key_code = key.value.vk
    # print(listener.canonical(key=key))
    print(key)

listener = keyboard.Listener(on_press=on_press)
listener.start()
try:
    while listener.is_alive():
        sleep(1)
except KeyboardInterrupt:
    listener.stop()