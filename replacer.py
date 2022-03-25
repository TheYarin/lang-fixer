from typing import Tuple

from utils import get_indexes, readFileFromAppFolder, reverse

layout1 = readFileFromAppFolder('layout1.txt')
layout2 = readFileFromAppFolder('layout2.txt')


def detectLayout(text: str) -> Tuple[str, str]:
    '''
    Returns (currentLayout, otherLayout)
    '''
    currentLayout = None
    otherLayout = None

    reversedText = reverse(text)

    for c in reversedText:
        if c in layout1 and c in layout2:
            continue
        elif c in layout1:
            currentLayout = layout1
            otherLayout = layout2
            break
        elif c in layout2:
            currentLayout = layout2
            otherLayout = layout1
            break

    return (currentLayout, otherLayout)


def replacer(text: str) -> str:
    currentLayout, otherLayout = detectLayout(text)

    if currentLayout is None:
        return text

    output = ''

    for c in text:
        indexes = get_indexes(c, currentLayout)

        if len(indexes) == 0:
            output += c
            continue

        index = indexes[0]  # TODO handle multiple indexes

        output += otherLayout[index]

    return output
