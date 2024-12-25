'''
You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visited them.
'''

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [(0,1), (1,0),(0,-1),(-1,0)]
        result = []

        steps =1
        x,y = rStart, cStart
        result.append([x,y])

        while len(result) < rows*cols:
            for i in range(4):

                dr, dc = directions[i]
                for _ in range(steps):
                    x += dr
                    y += dc
                    if 0 <= x < rows and 0 <= y < cols:
                        result.append([x,y])
                    
                if i % 2 == 1:
                    steps += 1
        return result
