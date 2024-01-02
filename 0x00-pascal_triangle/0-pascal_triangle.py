#!/usr/bin/python3
"""0-pascal_triangle"""


def pascal_triangle(n):
    """pascal triange
    Args:
        n (integer): number of rows

    Returns:
        list: pascal triangle
    """
    res = [[1]]
    if n <= 0:
        return []
    for i in range(n - 1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        res.append(row)
    return res
