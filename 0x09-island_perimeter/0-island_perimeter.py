#!/usr/bin/python3
"""
island perimeter module
"""


def island_perimeter(grid):
    """
    function that give the perimeter of island
    """

    rows, cols = len(grid), len(grid[0])

    largeur = 1
    longueur = 1
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                if (grid[row][col + 1] == 1 and col + 1 != cols):
                    largeur += 1
                if (grid[row + 1][col] == 1 and row + 1 != rows):
                    longueur += 1

    perimeter = (longueur + largeur) * 2
    return perimeter
