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
        winner = [[[0,0],[1,1],[2,2]] , [[0,0],[0,1],[0,2]], [[1,0],[1,1],[1,2]] ,[[2,0],[2,1],[2,2]], [[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]],[[1,1],[0,2],[2,0]]]


        playerA  = []
        playerB = []

        for i, move in enumerate(moves):
            if i % 2 == 0:
                playerA.append(move)
            else:
                playerB.append(move)
        def has_won(player_moves):
            for win_combo in winner:
                # Check if all moves in a winning combination are present
                if all(move in player_moves for move in win_combo):
                    return True
            return False

        # Check for winner
        if has_won(playerA):
            return "A"
        if has_won(playerB):
            return "B"

        # Check if game is still pending or ended in draw
        if len(moves) < 9:
            return "Pending"
        return "Draw"
