'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        numberOfIslands = 0

        def dfs(r, c):
            queue = collections.deque()

            queue.append((r,c))
            visited.add((r, c))

            while queue:
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                row, col = queue.popleft()
                for dr, dc in directions:
                    ra, ca = dr + row, dc + col

                    if (ra in range(rows) and 
                    ca in range(cols) and 
                    grid[ra][ca] == "1" and 
                    (ra,ca) not in visited):
                        queue.append((ra,ca))
                        visited.add((ra,ca))

        for r in range(rows):
            for c in range(cols):  
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    numberOfIslands += 1
        
        return numberOfIslands


