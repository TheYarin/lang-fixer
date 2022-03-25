import __main__
import sys
import os
import json
from typing import List

APP_FOLDER_PATH = None

if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app
    # path into variable _MEIPASS'.
    APP_FOLDER_PATH = sys._MEIPASS
else:
    APP_FOLDER_PATH = os.path.dirname(os.path.abspath(__main__.__file__))


def joinAppFolderPathAnd(subpath: str) -> str:
    return os.path.join(APP_FOLDER_PATH, subpath)


def readFile(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def readFileFromAppFolder(fileName: str) -> str:
    return readFile(joinAppFolderPathAnd(fileName))


def readJsonFile(filePath: str):
    with open(filePath, 'r') as f:
        return json.load(f)


def get_indexes(char: str, text: str) -> List[int]:
    return [i for i, c in enumerate(text) if c == char]


def reverse(text: str) -> str:
    return text[::-1]
