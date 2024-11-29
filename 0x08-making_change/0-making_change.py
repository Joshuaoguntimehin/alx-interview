#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the given amount total.

    Args:
        coins (list): The values of the coins in your possession.
        total (int): The total amount to meet.

    Returns:
        int: Fewest number of coins needed to meet the total, or -1 if not possible.
    """
    if total <= 0:
        return 0
    
    ''' Initialize an array to store the minimum coins needed for each value up to total'''
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make 0 total
    
    '''Iterate through all coin denominations'''
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    ''' If dp[total] is still float('inf'), it means the total cannot be met'''
    return dp[total] if dp[total] != float('inf') else -1
