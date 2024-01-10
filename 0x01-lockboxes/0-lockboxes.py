#!/usr/bin/python3
"""
determines if all boxes can be opened
"""

def canUnlockAll(boxes):
    """
    0. Lockboxes
    """
    if len(boxes) == 0:
        return False
    if len(boxes) == 1:
        return True
    keys = [0]
    for key in keys:
        for new_key in boxes[key]:
            if new_key not in keys and new_key < len(boxes):
                keys.append(new_key)
    if len(keys) == len(boxes):
        return True
    return False
