
from tkinter import *
from tkinter import ttk
from cgitb import text
from typing import Callable
import keyboard as kb


class OrderedSet:
    """
    A set that remembers the order items were added.
    """

    def __init__(self):
        self.data = {}

    def add(self, item):
        self.data[item] = None

    def remove(self, item):
        del self.data[item]

    def toList(self):
        return list(self.data.keys())

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data

    # def __iter__(self):
    #     return iter(self.data)


class Key:
    def __init__(self, scanCode, name):
        self.scanCode = scanCode
        self.name = name

    def __hash__(self):
        return self.scanCode

    def __eq__(self, other):
        return self.scanCode == other.scanCode


def listenForKeyCombination(callback: Callable) -> Callable:
    '''
    callback: a function that will be called when the key combination changes. The callback won't be called when a key is released, only when pressed. This callback will be passed a string representing the pressed keys. for example: 'ctrl+shift+a'

    Returns a function that can be called to stop listening for key presses.
    '''
    currentlyPressedKeys = OrderedSet()
    savedPressedKeysString = None

    def handleEvent(event):
        nonlocal savedPressedKeysString

        scanCode = event.scan_code
        eventType = event.event_type
        keyName = event.name.lower()

        key = Key(scanCode, keyName)

        if eventType == 'down':
            if key in currentlyPressedKeys:
                return

            currentlyPressedKeys.add(key)

            pressedKeysNames = [key.name for key in currentlyPressedKeys.toList()]
            savedPressedKeysString = '+'.join(pressedKeysNames)
            callback(savedPressedKeysString)
        elif eventType == 'up':
            currentlyPressedKeys.remove(key)

            if len(currentlyPressedKeys) == 0:
                savedPressedKeysString = None

    kb.hook(handleEvent)

    return lambda: kb.unhook(handleEvent)


# stop = listenForKeyCombination(lambda x: print(f'boom {x}'))
# kb.wait('esc')


# @@@@@@@@@@@@@@@@

window = Tk()
window.title("Welcome to TutorialsPoint")
window.geometry('400x400')
window.configure(background="grey")
a = Label(window, text="First Name")
a.grid(row=0, column=0)
listenForKeyCombination(lambda x: a.configure(text=x))

window.mainloop()


# @@@@@@@@@@@@@@@@
