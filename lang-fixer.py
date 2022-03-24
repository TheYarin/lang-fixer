import sys
from time import sleep
import keyboard as kb
from pynput.keyboard import Controller, Key
import pyperclip

from replacer import replacer

keyboardController = Controller()


def copySelectedText():
    copyKey = 'cmd' if sys.platform == 'darwin' else 'ctrl'
    kb.send(f'{copyKey}+c')


def changeLanguage():
    kb.send('alt+shift')  # TODO add support for macOS


def selectTextFromCursorToStartOfLine():
    # kb.send('shift+home') # doesn't work, a weird shift key up event of a shift key with scan code of 554 is sent immediately after the shift and it's weirdddd
    with keyboardController.pressed(Key.shift):  # Using pynput here because of the bug with the `keyboard` package
        keyboardController.tap(Key.home)
        keyboardController.tap(Key.home)  # again, to catch entire word-wrapped line


def on_hotkey():
    prevClipboardContent = pyperclip.paste()

    selectTextFromCursorToStartOfLine()

    copySelectedText()
    sleep(0.1)  # otherwise the copying may not be finished before pasting

    copiedText = pyperclip.paste()

    newText = replacer(copiedText)

    kb.write(newText)

    changeLanguage()
    pyperclip.copy(prevClipboardContent)


kb.add_hotkey('pause', on_hotkey)
kb.wait()
