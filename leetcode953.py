'''
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.

'''

from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Step 1: Create a dictionary mapping each character to its position in the alien alphabet
        hash_map = {c: i for i, c in enumerate(order)}
        
        # Step 2: Compare each adjacent pair of words
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            found_difference = False  # To track if we found a lexicographical difference
            
            for j in range(min(len(word1), len(word2))):
                if hash_map[word1[j]] < hash_map[word2[j]]:
                    found_difference = True  # Proper order, move to the next pair
                    break
                elif hash_map[word1[j]] > hash_map[word2[j]]:
                    return False  # Incorrect order
            
            # If no difference was found and word1 is longer than word2, it's incorrect
            if not found_difference and len(word1) > len(word2):
                return False
        
        return True
