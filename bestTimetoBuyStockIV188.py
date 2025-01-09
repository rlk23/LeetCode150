'''

Code
Testcase
Testcase
Test Result
188. Best Time to Buy and Sell Stock IV
Solved
Hard
Topics
Companies
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
 

Constraints:

1 <= k <= 100
1 <= prices.length <= 1000
0 <= prices[i] <= 1000

'''

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices) 

        if k >= n // 2:
            return sum(max(prices[i] - prices[i-1],0) for i in range(1,n))

        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]



        for t in range(k+1):
            dp[0][t][1] = -prices[0]
        for i in range(1,n):
            for t in range(1, k+1):
                dp[i][t][0] = max(dp[i-1][t][0] , dp[i-1][t][1] + prices[i])

                dp[i][t][1] = max(dp[i-1][t][1] , dp[i-1][t-1][0] - prices[i])
        
        return dp[n-1][k][0]
        
        
