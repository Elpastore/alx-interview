#!/usr/bin/python3
"""
making_change module
"""
import sys


def makeChange(coins, total):
    """
    makeChange function
    """
    if total <= 0:
        return 0
    dp = [sys.maxsize for i in range(total + 1)]
    dp[0] = 0
    m = len(coins)
    for i in range(1, total + 1):
        for j in range(m):
            if coins[j] <= i:
                subres = dp[i - coins[j]]
                if subres != sys.maxsize and subres + 1 < dp[i]:
                    dp[i] = subres + 1

    if dp[total] == sys.maxsize:
        return -1
    return dp[total]
