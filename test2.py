import keyboard as kb


def shiftHome():
    kb.press('shift')
    kb.press('home')
    kb.release('home')
    kb.release('shift')
    # kb.send('shift+home')
    # kb.send('shift+home') # again, to catch entire word-wrapped line


kb.add_hotkey('pause', shiftHome)
kb.wait()
