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

class Trie:
    def __init__(self):
        self.children = {}
        self.isAtEnd = False

        


class Solution:

    def build_trie(self, words):
        root = Trie()  # Initialize Trie root

        for word in words:  # Loop through each word in the list
            curr = root  # Start at root

            for c in word:  # Iterate over each character in the word
                if c not in curr.children:
                    curr.children[c] = Trie()  # Create a new Trie node if not exists
                curr = curr.children[c]  # Move to the next node
            
            curr.isAtEnd = True  # Mark end of word
        
        return root  

    def can_form(self,word, index, root,count):
        if index == len(word):
            return count >= 2
        
        curr  = root
        for i in range(index, len(word)):
            if word[i] not in curr.children:
                return False  # No valid path in Trie
            curr = curr.children[word[i]]

            if curr.isAtEnd:
                if self.can_form(word, i+1, root, count+1):
                    return True
        return False


    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        root = self.build_trie(words)
        result = []

        for word in words:
            if self.can_form(word, 0, root, 0):
                result.append(word)
        return result



        
