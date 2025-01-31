'''

Code
Testcase
Testcase
Test Result
1275. Find Winner on a Tic Tac Toe Game
Solved
Easy
Topics
Companies
Hint
Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

Players take turns placing characters into empty squares ' '.
The first player A always places 'X' characters, while the second player B always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never on filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.

'''

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # Initialize the number of moves
        num_moves = len(moves)
        # '\counters' is a list that holds the count of marks for each row, column and diagonals
        # indexes [0,1,2] are for rows, [3,4,5] are for columns, [6] is for diagonal, [7] is for anti-diagonal
        counters = [0] * 8

        # Start from the last move and check if there is a winner after every move
        for idx in range(num_moves - 1, -1, -2):
            # Get the row and column index from the last move
            row, col = moves[idx]
          
            # Increment the corresponding row and column counters
            counters[row] += 1
            counters[col + 3] += 1
          
            # If the move is on the main diagonal, increment the corresponding counter
            if row == col:
                counters[6] += 1
          
            # If the move is on the anti-diagonal, increment the corresponding counter
            if row + col == 2:
                counters[7] += 1
          
            # Check if any counters reached 3, which would indicate a win
            if any(value == 3 for value in counters):
                # Return 'B' if the current index is odd (indicating player "B"'s turn), otherwise 'A'
                return "B" if idx % 2 else "A"
      
        # After all moves, if no winner is found, check if the board is full. If yes, it's a draw
        # Otherwise, the game is still pending
        return "Draw" if num_moves == 9 else "Pending"
