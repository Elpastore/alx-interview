#!/usr/bin/python3
"""
island perimeter module
"""


def island_perimeter(grid):
    """
    function that give the perimeter of island
    """

    rows, cols = len(grid), len(grid[0])

    perimeter = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4
                if row < cols - 1 and grid[row + 1][col] == 1:
                    perimeter -= 2
                if col < rows - 1 and grid[row][col + 1] == 1:
                    perimeter -= 2

    return perimeter
