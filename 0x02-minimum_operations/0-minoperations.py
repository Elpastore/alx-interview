#!/usr/bin/python3
"""
0-minoperations module
"""


def minOperations(n):
    """
    method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    """
    if n == 1:
        return 0

    operations = 0
    h_count = 1
    clipboard = 0

    while h_count < n:
        if (n - h_count) % h_count == 0:
            clipboard = h_count
            operations += 2
            h_count *= 2
        else:
            operations += 1
            h_count += clipboard

    return operations
