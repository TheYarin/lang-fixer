#!/usr/bin/env python3

from time import sleep
import keyboard as kb
from pynput.keyboard import Controller, Key
import pyperclip

from settings import OS_SPECIFIC_HOTKEYS, TRIGGER_HOTKEY
from replacer import replacer


keyboardController = Controller()


def copySelectedText():
    copyHotkey = OS_SPECIFIC_HOTKEYS['COPY']
    kb.send(copyHotkey)


def changeLanguage():
    changeLanguageHotkey = OS_SPECIFIC_HOTKEYS['CHANGE_LANGUAGE']
    kb.send(changeLanguageHotkey)


def selectTextFromCursorToStartOfLine():
    # kb.send('shift+home') # doesn't work, a weird shift key up event of a shift key with scan code of 554 is sent immediately after the shift and it's weirdddd
    with keyboardController.pressed(Key.shift):  # Using pynput here because of the bug with the `keyboard` package
        keyboardController.tap(Key.home)
        keyboardController.tap(Key.home)  # again, to catch entire word-wrapped line


def on_hotkey():
    prevClipboardContent = pyperclip.paste()

    selectTextFromCursorToStartOfLine()

    copySelectedText()
    sleep(0.05)  # otherwise the copying may not be finished before pasting

    copiedText = pyperclip.paste()

    newText = replacer(copiedText)

    kb.write(newText)

    changeLanguage()
    pyperclip.copy(prevClipboardContent)


kb.add_hotkey(TRIGGER_HOTKEY, on_hotkey)
kb.wait()
