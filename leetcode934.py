'''
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.

'''

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        n = len(grid)

        directions = [[1,0],[0,1], [-1,0],[0,-1]]

        first_island = set()

        def dfs(x,y):
            if x < 0 or x >= n or y < 0 or y >= n or grid[x][y] != 1:
                return
            
            grid[x][y] = -1
            first_island.add((x,y))
            for dx, dy in directions:
                dfs(x+dx, y +dy)
        


        def find_first_island():
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        dfs(i,j)
                        return
        
        find_first_island()

        queue = deque(first_island)
        steps = 0

        while queue:
            for _ in range(len(queue)):
                x,y = queue.popleft()
                for dr, dc in directions:
                    new_x, new_y = dr + x, dc + y

                    if 0 <= new_x < n and 0 <= new_y < n:
                        if grid[new_x][new_y] == 1:
                            return steps
                        
                        if grid[new_x][new_y] == 0:
                            grid[new_x][new_y] = -1
                            queue.append((new_x,new_y))
            steps += 1

        return -1
