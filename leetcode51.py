'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9

'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row):
            if row == n:
                board = ["".join(row) for row in board_state]
                result.append(board)
                return 
            for col in range(n):
                if col in cols or (row-col) in diag1 or (row+col) in diag2:
                    continue
                

                board_state[row][col] = "Q"
                cols.add(col)
                diag1.add(row-col)
                diag2.add(row+col)

                backtrack(row+1)

                board_state[row][col] = "."
                cols.remove(col)
                diag1.remove(row-col)
                diag2.remove(row+col)

        result = []
        board_state = [["."] * n  for _ in range(n)]
        cols, diag1, diag2 = set(), set(), set()

        backtrack(0)
        return result
