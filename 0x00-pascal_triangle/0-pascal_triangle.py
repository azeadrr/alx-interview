#!/usr/bin/python3
"""function def pascal_triangle(n): that returns
a list of lists of integers"""

def pascal_triangle(n):
    """
    0. Pascal's Triangle
    """
    res = [[1]]
    if num <= 0:
        return []
    for i in range(num - 1):
        tmp = [0] + res[-1] + [0]
        row = []
        for x in range(len(res[-1]) + 1):
            row.append(tmp[x] + tmp[x + 1])
        res.append(row)
    return res
