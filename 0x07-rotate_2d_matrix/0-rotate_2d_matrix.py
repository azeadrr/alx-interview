#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """n x n 2D matrix, rotate it 90 degrees clockwise"""
    n = len(matrix)
    temp = matrix[:]
    for y in range(n):
        dd = []
        for x in range(n-1, -1, -1):
            dd.append(matrix[x][y])
        matrix.append(dd)
    for dd in temp:
        matrix.pop(matrix.index(dd))
