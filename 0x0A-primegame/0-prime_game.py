#!/usr/bin/python3
"""function to  find winner"""
def isWinner(x, nums):
    """Determine the winner of the game after x rounds."""
    if x < 1 or not nums:
        return None

    # Find the maximum number in nums to precompute primes
    max_n = max(nums)

    # Step 1: Precompute primes using a sieve
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    # Step 2: Count primes up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Step 3: Determine the winner for each round
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        # Number of primes up to n
        primes_up_to_n = prime_count[n]
        # Maria wins if the number of primes is odd, otherwise Ben wins
        if primes_up_to_n % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Step 4: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
      