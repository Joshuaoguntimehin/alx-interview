#!/usr/bin/python3
"""making changes"""
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    
    Args:
        coins (list): List of coin values.
        total (int): The target total amount.
        
    Returns:
        int: Fewest number of coins needed to meet the total,
             or -1 if the total cannot be met.
    """
    if total <= 0:
        return 0
    
    # Sort coins in descending order for optimization
    coins.sort(reverse=True)
    count = 0
    remaining = total

    for coin in coins:
        if remaining <= 0:
            break
        num_coins = remaining // coin
        count += num_coins
        remaining -= num_coins * coin

    # If there is still some amount remaining, return -1
    if remaining > 0:
        return -1
    
    return count
