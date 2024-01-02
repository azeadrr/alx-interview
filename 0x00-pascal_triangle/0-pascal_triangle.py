#!/usr/bin/python3
"""function that returns
a list of lists of integers"""


def pascal_triangle(n):
    """pascal triange
    """
    res = [[1]]
    if num <= 0:
        return []
    for i in range(num - 1):
        temp = [0] + res[-1] + [0]
        row = []
        for x in range(len(res[-1]) + 1):
            row.append(temp[x] + temp[x + 1])
        res.append(row)
    return res
