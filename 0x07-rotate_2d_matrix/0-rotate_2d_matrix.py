#!/usr/bin/python3
"""
0-rotate_2d_matrix module
"""


def rotate_2d_matrix(matrix):
    n = len(matrix)

    # Step 1: Transpose the matrix (swap rows with columns)
    for row in range(n):
        for col in range(row, n):
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = matrix[row][col]

    # Step 2: Reverse each row
    for row in range(n):
        matrix[row].reverse()
