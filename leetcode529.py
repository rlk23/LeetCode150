'''
Let's play the minesweeper game (Wikipedia, online game)!

You are given an m x n char matrix board representing the game board where:

'M' represents an unrevealed mine,
'E' represents an unrevealed empty square,
'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
'X' represents a revealed mine.
You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').

Return the board after revealing this position according to the following rules:

If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.
 

Example 1:

'''

from collections import deque
from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows, cols = len(board), len(board[0])
        r, c = click  # Click position
        
        # If the clicked cell is a mine, game over
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        
        # Directions: up, down, left, right, and diagonals
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),         (0, 1),
                      (1, -1), (1, 0), (1, 1)]
        
        # BFS to reveal the board
        queue = deque([(r, c)])
        while queue:
            row, col = queue.popleft()
            
            # Count adjacent mines
            mine_count = 0
            for dr, dc in directions:
                new_r, new_c = row + dr, col + dc
                if 0 <= new_r < rows and 0 <= new_c < cols and board[new_r][new_c] == 'M':
                    mine_count += 1

            # If there are adjacent mines, show count
            if mine_count > 0:
                board[row][col] = str(mine_count)
            else:
                # If no adjacent mines, mark as 'B' and reveal neighbors
                board[row][col] = 'B'
                for dr, dc in directions:
                    new_r, new_c = row + dr, col + dc
                    if (0 <= new_r < rows and 0 <= new_c < cols and board[new_r][new_c] == 'E'):
                        queue.append((new_r, new_c))
                        board[new_r][new_c] = 'B'  # Prevents re-adding the same cell
        
        return board
