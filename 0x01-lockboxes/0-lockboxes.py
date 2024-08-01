#!/usr/bin/python3
'''determines if all the boxes can be opened'''


def canUnlockAll(boxes):
    '''check boxes'''
    n = len(boxes)
    opened = set()
    line = [0]

    for key in line:
        if key not in opened:
            opened.add(key)
            for bx in boxes[key]:
                if bx < n and bx not in opened:
                    line.append(bx)

    return len(opened) == n
