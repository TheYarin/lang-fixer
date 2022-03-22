import sys
from time import sleep
from pynput.keyboard import Key, Controller, Listener, GlobalHotKeys
import pyperclip

from replacer import replacer

keyboardController = Controller()

def changeLanguage():
    # TODO add mac/linux support
    with keyboardController.pressed(Key.alt_l):
        keyboardController.tap(Key.shift_l)

def on_activate():
    '''Defines what happens on press of the hotkey'''
    print("Activated!")
    prevClipboardContent = pyperclip.paste()

    # Select from cursor to home
    with keyboardController.pressed(Key.shift):
        keyboardController.tap(Key.home)
        keyboardController.tap(Key.home) # again, to catch entire word-wrapped line

    # Copy
    copyKey = Key.cmd if sys.platform == 'darwin' else Key.ctrl
    with keyboardController.pressed(copyKey):
        keyboardController.tap('c')

    sleep(0.1) # otherwise the copying may not be finished before pasting

    copiedText = pyperclip.paste()

    newText = replacer(copiedText)
    keyboardController.type(newText)
    changeLanguage() # cannot happen before the call to type() because it interprets some keys wrongfully, like comma (,) (will be translated to ת instead of ')
    
    # for char in copiedText:
    #     keyboardController.tap(char)
    
    
    # TODO only write hebrew with hebrew layout. anything else should be written with the english layout. because bugs.

    pyperclip.copy(prevClipboardContent)

def for_canonical(hotkey):
    '''Removes any modifier state from the key events 
    and normalises modifiers with more than one physical button'''
    return lambda k: hotkey(Listener.canonical(k))

'''Creating the hotkey'''
# hotkey = HotKey(
# HotKey.parse('<shift>+k'), 
# on_activate)

# with Listener(
#         on_press=for_canonical(hotkey.press),
#         on_release=for_canonical(hotkey.release)) as listener:
#     listener.join()

with GlobalHotKeys({
        '<19>': on_activate}) as hotKeysListener:
    # hotKeysListener.join()
    # hotKeysListener.start()
    try:
        while hotKeysListener.is_alive():
            sleep(1)
    except KeyboardInterrupt:
        hotKeysListener.stop()