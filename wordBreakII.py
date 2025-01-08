'''
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
 

Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
Input is generated in a way that the length of the answer doesn't exceed 105.

'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        return self.helper(s, wordDict, 0, memo)

    def helper(self,s, wordDict, start, memo):
        if start == len(s):
            return [""]
            
        if start in memo:
            return memo[start]
            
        sentences = []

        for word in wordDict:
            if s[start:start+len(word)] == word:
                sub_sentences = self.helper(s, wordDict, start + len(word),memo)
                for sentence in sub_sentences:
                    if sentence:
                        sentences.append(word + " " + sentence)
                    else:
                        sentences.append(word)
        memo[start] = sentences
        return sentences

