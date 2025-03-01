'''
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.

'''
from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_id = 2  # Start labeling from 2 to avoid confusion with 1s
        island_sizes = {0: 0}  # Dictionary to store island sizes

        # Directions for moving in 4 directions (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Step 1: DFS to label each island and calculate its size
        def dfs(r, c):
            if r < 0 or c < 0 or r >= n or c >= n or grid[r][c] != 1:
                return 0
            grid[r][c] = island_id  # Mark with unique island ID
            size = 1  # Start counting size
            for dr, dc in directions:
                size += dfs(r + dr, c + dc)
            return size

        # Step 2: Identify all islands and store their sizes
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    island_sizes[island_id] = dfs(r, c)
                    island_id += 1  # Move to next unique island ID

        # Step 3: Find the largest island if we flip one 0 to 1
        max_size = max(island_sizes.values(), default=0)  # Base case if grid is all 1s

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    # Collect unique neighboring islands
                    neighboring_islands = set()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            neighboring_islands.add(grid[nr][nc])

                    # Compute new possible island size
                    new_size = 1  # The converted '0' itself
                    for island in neighboring_islands:
                        new_size += island_sizes[island]

                    max_size = max(max_size, new_size)  # Update max possible island size

        return max_size
