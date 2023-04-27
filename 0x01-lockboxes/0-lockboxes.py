#!/usr/bin/python3
def canUnlockAll(boxes):
    """Determines if all boxes can be opened"""
    num_boxes = len(boxes)
    unlocked = set([0])
    keys = boxes[0]

    while keys:
        box = keys.pop()
        if box < num_boxes and box not in unlocked:
            unlocked.add(box)
            keys.extend(boxes[box])

    return len(unlocked) == num_boxes
