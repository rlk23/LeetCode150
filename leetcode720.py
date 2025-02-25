'''
Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

Note that the word should be built from left to right with each additional character being added to the end of a previous word. 

 

Example 1:

Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:

Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 30
words[i] consists of lowercase English letters.
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isAtEnd = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isAtEnd = True

    def longest_word(self):
        stack = [(self.root, "")]  # (current node, word formed so far)
        result = ""

        while stack:
            node, word = stack.pop()

            if len(word) > len(result) or (len(word) == len(result ) and word < result):
                result = word
            
            for char in sorted(node.children.keys(), reverse=True):
                if node.children[char].isAtEnd:
                    stack.append((node.children[char], word + char))

        return result



class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)

        return trie.longest_word()
