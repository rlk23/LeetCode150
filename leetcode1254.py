'''
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1

'''

from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        closed_islands = 0

        def dfs(r, c):
            # If we're out of bounds, this island touches the border
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            
            # If it's water, stop DFS here
            if grid[r][c] == 1:
                return True
            
            # Mark the land as visited by converting it to water
            grid[r][c] = 1
            
            # Explore in all four directions
            top = dfs(r - 1, c)
            bottom = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            
            # This land is part of a closed island if **all** directions are surrounded by water
            return top and bottom and left and right

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:  # Found land
                    if dfs(r, c):    # Only increment if DFS confirms it's a closed island
                        closed_islands += 1

        return closed_islands
