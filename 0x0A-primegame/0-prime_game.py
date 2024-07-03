#!/usr/bin/python3
"""
0-prime_game module
"""


def isWinner(x, nums):
    """
    prime game algo
    """
    if x <= 0 or not nums:
        return None

    def sieve(max_n):
        """
        Sieve of Eratosthenes algo
        """
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False
        p = 2
        while (p * p <= max_n):
            if (is_prime[p]):
                for i in range(p * p, max_n + 1, p):
                    is_prime[i] = False
            p += 1
        return is_prime

    max_n = max(nums)
    is_prime = sieve(max_n)

    def find_winner(n):
        """
        find the winner
        """
        if n < 2:
            return "Ben"

        primes_count = sum(is_prime[2:n+1])
        return "Maria" if primes_count % 2 != 0 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = find_winner(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
