'''

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
 

Note: This question is the same as 1765: https://leetcode.com/problems/map-of-highest-peak/
'''

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        queue = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r,c))

                else:
                    mat[r][c] = float("inf")

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                new_x, new_y = dr + r, dc + c

                if 0 <= new_x < rows and 0 <= new_y < cols and mat[new_x][new_y] > mat[r][c] + 1:
                   mat[new_x][new_y] = mat[r][c] + 1  # Update distance
                   queue.append((new_x,new_y))
        return mat
