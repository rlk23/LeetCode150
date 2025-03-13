'''
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words (not necessarily distinct) in the given array.

 

Example 1:

Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Example 2:

Input: words = ["cat","dog","catdog"]
Output: ["catdog"]
 

Constraints:

1 <= words.length <= 104
1 <= words[i].length <= 30
words[i] consists of only lowercase English letters.
All the strings of words are unique.
1 <= sum(words[i].length) <= 105

'''

from typing import List

class Trie:
    def __init__(self):
        self.children = {}
        self.isAtEnd = False

class Solution:
    def insert_into_trie(self, word, root):
        curr = root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.isAtEnd = True  

    def can_form(self, index, word, root, memo, count):
        if index == len(word):
            return count >= 2  

        if index in memo:  
            return memo[index]

        curr = root
        for i in range(index, len(word)):
            if word[i] not in curr.children:
                memo[index] = False  
                return False
            curr = curr.children[word[i]]

            if curr.isAtEnd:
                if self.can_form(i+1, word, root, memo, count+1):
                    memo[index] = True  
                    return True

        memo[index] = False
        return False

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)  
        trie = Trie()
        result = []

        for word in words:
            if self.can_form(0, word, trie, {}, 0):  
                result.append(word)
            else:
                self.insert_into_trie(word, trie)  

        return result




        
