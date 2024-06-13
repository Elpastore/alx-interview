#!/usr/bin/python3
"""
0-rotate_2d_matrix module
"""


def rotate_2d_matrix(matrix):
    """
    rotate a matrix
    """
    n = len(matrix)
    for row in range(n):
        for col in range(row, n):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
    for row in matrix:
        row.reverse()
