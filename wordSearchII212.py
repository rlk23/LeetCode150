'''
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.


'''
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def build_trie(words):
            root = {}
            for word in words:
                node = root
                for char in word:
                    if char not in node:
                        node[char] = {}
                    node = node[char]
                node["#"] = True  # Mark the end of a word
            return root

        def dfs(x, y, node, path):
            char = board[x][y]
            if char not in node:
                return
            next_node = node[char]
            path += char
            if "#" in next_node:
                result.add(path)  # Found a word
            
            board[x][y] = "0"  # Mark the cell as visited
            for dr, dc in directions:
                nx, ny = x + dr, y + dc
                if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] != "0":
                    dfs(nx, ny, next_node, path)
            board[x][y] = char  # Restore the cell
        
        # Main Logic
        rows, cols = len(board), len(board[0])
        trie = build_trie(words)
        result = set()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Directions: up, right, down, left

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie:
                    dfs(r, c, trie, "")
        
        return list(result)

      
