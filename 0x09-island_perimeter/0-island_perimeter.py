#!/usr/bin/python3
"""
Island perimeter module
"""


def island_perimeter(grid):
    """
    Function that calculates the perimeter of an island
    """

    rows, cols = len(grid), len(grid[0])

    perimeter = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4
                if row < rows - 1 and grid[row + 1][col] == 1:
                    perimeter -= 2
                if col < cols - 1 and grid[row][col + 1] == 1:
                    perimeter -= 2

    return perimeter
