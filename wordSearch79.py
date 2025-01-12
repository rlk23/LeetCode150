'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?

'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search_word(x: int, y: int, index: int) -> bool:
            # Check if the last character matches 
            if index == len(word) - 1:
                return board[x][y] == word[index]
            # If current character does not match the word character at index, return False
            if board[x][y] != word[index]:
                return False
            # Store the current character and mark the cell as visited with "0"
            temp = board[x][y]
            board[x][y] = "0"
            # Define directions for exploration: up, right, down, left
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            # Loop through all possible directions
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                # Check boundaries and if the next cell is not visited
                if 0 <= new_x < rows and 0 <= new_y < cols and board[new_x][new_y] != "0":
                    # Recur with the new position and the next character index
                    if search_word(new_x, new_y, index + 1):
                        return True
            # Restore the current cell's value after exploring all directions
            board[x][y] = temp
            return False

        # Retrieve the dimensions of the board
        rows, cols = len(board), len(board[0])
        # Iterate through each cell in the board, trying to match the first character
        for i in range(rows):
            for j in range(cols):
                # If the first character matches and the word can be found from here, return True
                if board[i][j] == word[0] and search_word(i, j, 0):
                    return True
        # If the word cannot be found, return False
        return False
