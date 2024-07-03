#!/usr/bin/python3
"""
0-prime_game module
"""


def generate_primes(n):
    """Generate a list of primes up to n using the Sieve of Eratosthenes."""
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p) <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    arrayPrime = [p for p in range(2, n + 1) if prime[p]]
    return arrayPrime


def simulate_game(n):
    """
    Simulate the game for a given n and determine the winner.
    """
    primes = generate_primes(n)
    available_numbers = [True] * (n + 1)
    turn = 0

    for prime in primes:
        if available_numbers[prime]:
            for multiple in range(prime, n + 1, prime):
                available_numbers[multiple] = False
            turn ^= 1

    return "Ben" if turn == 0 else "Maria"


def isWinner(x, nums):
    """
    prime game algo
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = simulate_game(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
