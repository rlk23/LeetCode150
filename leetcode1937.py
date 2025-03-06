'''
You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.

abs(x) is defined as:

x for x >= 0.
-x for x < 0.
 

Example 1:


Input: points = [[1,2,3],[1,5,1],[3,1,1]]
Output: 9
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
You add 3 + 5 + 3 = 11 to your score.
However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
Your final score is 11 - 2 = 9.
Example 2:


Input: points = [[1,5],[2,3],[4,2]]
Output: 11
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 1), (1, 1), and (2, 0).
You add 5 + 3 + 4 = 12 to your score.
However, you must subtract abs(1 - 1) + abs(1 - 0) = 1 from your score.
Your final score is 12 - 1 = 11.
 

Constraints:

m == points.length
n == points[r].length
1 <= m, n <= 105
1 <= m * n <= 105
0 <= points[r][c] <= 105


'''

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])

        # Initialize dp with the first row
        dp = points[0]

        for r in range(1, m):
            left_max = [0] * n
            right_max = [0] * n
            new_dp = [0] * n

            # Left to Right Sweep (Compute max left values)
            left_max[0] = dp[0]
            for c in range(1, n):
                left_max[c] = max(left_max[c-1] - 1, dp[c])  # Penalize moving right

            # Right to Left Sweep (Compute max right values)
            right_max[-1] = dp[-1]
            for c in range(n-2, -1, -1):
                right_max[c] = max(right_max[c+1] - 1, dp[c])  # Penalize moving left

            # Compute new dp values for row r
            for c in range(n):
                new_dp[c] = points[r][c] + max(left_max[c], right_max[c])

            # Update dp for the next row
            dp = new_dp

        return max(dp)

