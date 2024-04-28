#!/usr/bin/python3
"""
0-pascal_triangle module
"""


def pascal_triangle(n):
    """
    Pascla's triangle of n
    """
    if n <= 0:
        return []

    triangle = []

    for x in range(n):
        row = []

        for y in range(x + 1):
            if y == 0 or y == x:
                row.append(1)
            else:
                value = triangle[x - 1][y - 1] + triangle[x - 1][y]
                row.append(value)

        triangle.append(row)

    return triangle
