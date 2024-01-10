#!/usr/bin/python3
"""
that determines if all boxes
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
        for nkey in boxes[key]:
            if nkey not in keys and nkey < len(boxes):
                keys.append(nkey)
    if len(keys) == len(boxes):
        return True
    return False
