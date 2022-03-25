import sys

from utils import joinAppFolderPathAnd, readJsonFile

settingsFilePath = joinAppFolderPathAnd('settings.json')

SETTINGS = readJsonFile(settingsFilePath)

TRIGGER_HOTKEY = SETTINGS['TRIGGER_HOTKEY']

OS_SPECIFIC_HOTKEYS = None

if sys.platform == 'linux':
    OS_SPECIFIC_HOTKEYS = SETTINGS['OS_SPECIFIC']['LINUX']
elif sys.platform == 'darwin':
    OS_SPECIFIC_HOTKEYS = SETTINGS['OS_SPECIFIC']['MAC_OS']
elif sys.platform == 'win32':
    OS_SPECIFIC_HOTKEYS = SETTINGS['OS_SPECIFIC']['WINDOWS']

if not OS_SPECIFIC_HOTKEYS:
    print('Error: Your OS is not supported')
    sys.exit(1)
