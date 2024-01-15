#!/usr/bin/python3
"""minoperations"""


def minOperations(n):
    """minOperations function"""
    paste = 1
    clipbrd = 0
    cntr = 0

    while paste < n:
        if clipbrd == 0:
            clipbrd = paste
            cntr += 1

        if paste == 1:
            paste += clipbrd
            cntr += 1
            continue
        remaining = n - paste

        if remaining < clipbrd:
            return 0

        if remaining % paste != 0:
            paste += clipbrd
            cntr += 1
        else:
            clipbrd = paste
            paste += clipbrd
            cntr += 2

    if paste == n:
        return cntr
    else:
        return 0
