'''
Longest Increasing Path
Medium
Find the longest strictly increasing path in a matrix of positive integers. A path is a sequence of cells where each one is 4-directionally adjacent (up, down, left, or right) to the previous one.

Example:


Output: 5
'''
from typing import List
from collections import deque

def longest_increasing_path(matrix: List[List[int]]) -> int:
    # Write your code here
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Memoization table to store longest path for each cell
    memo = [[-1] * cols for _ in range(rows)]

    def dfs(r, c):
        if memo[r][c] != -1:
            return memo[r][c]

        max_length = 1  # At minimum, each cell itself is a path of length 1

        for dr, dc in directions:
            new_x, new_y = r + dr, c + dc
            if (0 <= new_x < rows and 0 <= new_y < cols and matrix[new_x][new_y] > matrix[r][c]):
                max_length = max(max_length, 1 + dfs(new_x, new_y))
        
        memo[r][c] = max_length  # Store result in memoization table
        return memo[r][c]

    # Find longest increasing path starting from every cell
    return max(dfs(r, c) for r in range(rows) for c in range(cols))
