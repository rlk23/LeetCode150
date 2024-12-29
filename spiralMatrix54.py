'''
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix), len(matrix[0])

        left, right = 0, len(matrix[0])
        up, down = 0, len(matrix)
        res = []

        while left < right and up < down:

            for i in range(left, right):
                res.append(matrix[up][i])
            
            up += 1

            for i in range(up, down):
                res.append(matrix[i][right-1])
            
            right -= 1

            if not (left <right and up < down):
                break
            
            for i in range(right-1,left-1,-1):
                res.append(matrix[down-1][i])

            down -= 1

            for i in range(down-1, up-1,-1):
                res.append(matrix[i][left])
            
            left += 1
        return res
