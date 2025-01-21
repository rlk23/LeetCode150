'''
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

 

Example 1:


Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
Example 2:


Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
Output: -1
Explanation: We need to eliminate at least two obstacles to find such a walk.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 40
1 <= k <= m * n
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 0

'''
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])

        if rows == 1 and cols == 1:
            return 0
        queue = collections.deque([(0,0,k,0)])
        visited = set([(0,0,k)])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r,c ,remain_steps, step = queue.popleft()

            for dr, dc in directions:
                new_x, new_y = dr + r, dc + c

                if 0 <= new_x < rows and 0 <= new_y < cols:
                    if new_x == rows - 1 and new_y == cols - 1:
                        return step + 1
                    
                
                    if grid[new_x][new_y] == 1 and remain_steps > 0:
                        new_state = (new_x, new_y, remain_steps-1)
                        if new_state not in visited:
                            visited.add(new_state)
                            queue.append((new_x,new_y,remain_steps-1, step+1))
                    elif grid[new_x][new_y] == 0:
                        new_state = (new_x, new_y, remain_steps)
                        if new_state not in visited:
                            visited.add(new_state)
                            queue.append((new_x, new_y, remain_steps, step+1))
        return -1

