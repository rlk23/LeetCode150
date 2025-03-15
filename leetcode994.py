'''

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

'''

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        fresh_count = 0
        queue = deque()

        # Initialize the queue with all initially rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # Add (row, col, time)
                elif grid[r][c] == 1:
                    fresh_count += 1  # Count fresh oranges

        time = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        # BFS traversal
        while queue:
            r, c, curr_time = queue.popleft()  # Extract current time from the queue
            time = max(time, curr_time)  # Update time with the maximum value

            for dr, dc in directions:
                new_x, new_y = r + dr, c + dc

                if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == 1:
                    grid[new_x][new_y] = 2  # Rot the fresh orange
                    fresh_count -= 1
                    queue.append((new_x, new_y, curr_time + 1))  # Increment time

        return time if fresh_count == 0 else -1  # If all fresh oranges are rotten, return time; otherwise, return -1

