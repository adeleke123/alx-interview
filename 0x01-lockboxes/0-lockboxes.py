#!/usr/bin/python3
def canUnlockAll(boxes):
    """Determines if all boxes can be opened"""
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
