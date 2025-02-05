'''
You are given an array of coin values and a target amount of money. Return the minimum number of coins needed to total the target amount. If this isn't possible, return ‐1. You may assume there's an unlimited supply of each coin.

Example 1:
Input: coins = [1, 2, 3], target = 5
Output: 2
Explanation: Use one 2-dollar coin and one 3-dollar coin to make 5 dollars.

Example 2:
Input: coins = [2, 4], target = 5
Output: -1

'''

from typing import List

def min_coin_combination(coins: List[int], target: int) -> int:
    # Write your code here
    if target == 0:
        return 0

    dp = [float("inf")] * (target + 1)
    dp[0] = 0


    for i in range(1, target+1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i-coin] +1)
    return dp[target] if dp[target]!= float('inf') else -1
