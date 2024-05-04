#!/usr/bin/env python3
"""
lockboxes module
"""


def canUnlockAll(boxes):
    """
    function that check if all boxes can be uncloked
    args:
        -boxes: list of integer
    Return:
        -True if all boxes can be unloked
        -False not all boxes can be unlocked
    """
    unLocked = set()
    unLocked.add(0)  # Start by unlocking the first box
    keys = set(boxes[0])  # Keys from the first box

    while keys:
        new_keys = set()
        for key in keys:
            if key < len(boxes) and key not in unLocked:
                unLocked.add(key)
                new_keys.update(boxes[key])  # add new keys from unlocked boxes
        keys = new_keys  # new keys to be iterated

    return len(unLocked) == len(boxes)
