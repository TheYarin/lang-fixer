from typing import List, Tuple


def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

layout1 = read_file('./layout1.txt')
layout2 = read_file('./layout2.txt')

def get_indexes(char: str, text: str) -> List[int]:
    return [i for i, c in enumerate(text) if c == char]

#reverse string
def reverse(text: str) -> str:
    return text[::-1]

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

        index = indexes[0] # TODO handle multiple indexes

        output += otherLayout[index]

    return output

