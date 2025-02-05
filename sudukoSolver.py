'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:



'''

import collections
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solves the Sudoku puzzle in-place using backtracking.
        """
        def is_valid(row, col, num):
            """Check if `num` can be placed at board[row][col]."""
            return (num not in rows[row] and
                    num not in cols[col] and
                    num not in squares[(row // 3, col // 3)])
                
        def insert(row, col, num):
            """Insert `num` into the board and tracking sets."""
            board[row][col] = str(num)
            rows[row].add(num)
            cols[col].add(num)
            squares[(row // 3, col // 3)].add(num)

        def remove(row, col, num):
            """Remove `num` (backtrack) from board and tracking sets."""
            board[row][col] = "."
            rows[row].remove(num)
            cols[col].remove(num)
            squares[(row // 3, col // 3)].remove(num)

        def backtrack():
            """Backtracking function to solve Sudoku."""
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for num in range(1, 10):  # Try numbers 1-9
                            if is_valid(r, c, num):
                                insert(r, c, num)

                                if backtrack():  # Recursive call
                                    return True
                                
                                remove(r, c, num)  # Undo move (backtrack)
                        
                        return False  # No valid number found, backtrack
            return True  # Sudoku is solved

        # Initialize tracking sets for rows, columns, and 3×3 subgrids
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        # Populate sets with existing numbers
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    num = int(board[r][c])  # Convert string to integer
                    rows[r].add(num)
                    cols[c].add(num)
                    squares[(r // 3, c // 3)].add(num)

        # Start solving Sudoku
        backtrack()
