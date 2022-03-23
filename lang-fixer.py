import sys
from time import sleep
from typing import Union
from pynput.keyboard import Key, Controller, Listener, GlobalHotKeys
import pyperclip

from replacer import replacer, layout1, detectLayout

keyboardController = Controller()

class LayoutAwareTyper:
    def __init__(self, currentLayout):
        self._isEnglish = currentLayout == layout1
        self._initialIsEnglish = self._isEnglish

    def type(self, text):
        for c in text:
            if c in layout1:
                self._switchToEnglish()
            else:
                self._switchToHebrew()

            keyboardController.tap(c)
    
    def _changeLanguage(self):
        # TODO add mac/linux support
        with keyboardController.pressed(Key.alt_l):
            keyboardController.tap(Key.shift_l)
        self._isEnglish = not self._isEnglish
    
    def _switchToEnglish(self):
        if not self._isEnglish:
            self._changeLanguage()
    
    def _switchToHebrew(self):
        if self._isEnglish:
            self._changeLanguage()

    def switchToOtherLayout(self):
        if (self._initialIsEnglish):
            self._switchToHebrew()
        else:
            self._switchToEnglish()

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

    currentLayout, _ = detectLayout(copiedText)
    layoutAwareTyper = LayoutAwareTyper(currentLayout)
    layoutAwareTyper.type(newText)
    layoutAwareTyper.switchToOtherLayout()
    
    # TODO only write hebrew with hebrew layout. anything else should be written with the english layout. because bugs.

    pyperclip.copy(prevClipboardContent)

with GlobalHotKeys({'<19>': on_activate}) as hotKeysListener:
    try:
        while hotKeysListener.is_alive():
            sleep(1)
    except KeyboardInterrupt:
        hotKeysListener.stop()