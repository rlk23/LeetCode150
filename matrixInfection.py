'''
Matrix Infection
Medium
You are given a matrix where each cell is either:

0: Empty
1: Uninfected
2: Infected

With each passing second, every infected cell (2) infects its uninfected neighboring cells (1) that are 4-directionally adjacent. Determine the number of seconds required for all uninfected cells to become infected. If this is impossible, return ‐1.

Example:


Input: matrix = [[1, 1, 1, 0], [0, 0, 2, 1], [0, 1, 1, 0]]
Output: 3

'''

from typing import List
from collections import defaultdict
from collections import deque

def matrix_infection(matrix: List[List[int]]) -> int:
    # Write your code here
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    directions = [[1,0],[0,1], [-1,0],[0,-1]]



    queue = deque()
    count_uninfected = 0

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 2:
                queue.append((r,c,0))
            elif matrix[r][c] == 1:
                count_uninfected += 1
    if count_uninfected == 0:
        return 0

    timer= 0 
    directions = [[1,0],[0,1],[-1,0],[0,-1]]

    while queue:
        r,c , time = queue.popleft()

        timer = max(time, timer)

        for dr, dc in directions:
            new_x, new_y = dr + r, dc+ c

            if 0 <= new_x < rows and 0 <= new_y < cols and matrix[new_x][new_y] == 1:
                matrix[new_x][new_y] = 2
                count_uninfected -= 1
                queue.append((new_x,new_y,time+1))
    return timer if count_uninfected == 0 else -1



