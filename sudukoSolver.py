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
        Solves the Sudoku puzzle in-place using optimized backtracking.
        """
        def is_valid(row, col, num):
            """Check if `num` can be placed at board[row][col]."""
            return not (rows[row][num] or cols[col][num] or squares[(row // 3, col // 3)][num])
                
        def insert(row, col, num):
            """Insert `num` into the board and tracking sets."""
            board[row][col] = str(num)
            rows[row][num] = True
            cols[col][num] = True
            squares[(row // 3, col // 3)][num] = True

        def remove(row, col, num):
            """Remove `num` (backtrack) from board and tracking sets."""
            board[row][col] = "."
            rows[row][num] = False
            cols[col][num] = False
            squares[(row // 3, col // 3)][num] = False

        def backtrack(index):
            """Backtracking function to solve Sudoku using precomputed empty cells."""
            if index == len(empty_cells):  # Base case: all cells filled
                return True
            
            row, col = empty_cells[index]
            for num in range(1, 10):  # Try numbers 1-9
                if is_valid(row, col, num):
                    insert(row, col, num)
                    
                    if backtrack(index + 1):  # Recursive call
                        return True
                    
                    remove(row, col, num)  # Undo move (backtrack)
            
            return False  # No valid number found, backtrack

        # Use boolean arrays instead of sets for quick lookup
        rows = [collections.defaultdict(bool) for _ in range(9)]
        cols = [collections.defaultdict(bool) for _ in range(9)]
        squares = {(i, j): collections.defaultdict(bool) for i in range(3) for j in range(3)}
        
        empty_cells = []

        # Populate sets with existing numbers and track empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty_cells.append((r, c))  # Store empty cell positions
                else:
                    num = int(board[r][c])
                    rows[r][num] = True
                    cols[c][num] = True
                    squares[(r // 3, c // 3)][num] = True

        # Start solving Sudoku using backtracking with empty cell list
        backtrack(0)
