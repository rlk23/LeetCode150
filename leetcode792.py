'''
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
Example 2:

Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
 

Constraints:

1 <= s.length <= 5 * 104
1 <= words.length <= 5000
1 <= words[i].length <= 50


'''

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        charMap = collections.defaultdict(list)

        for i, char in enumerate(s):
            charMap[char].append(i)


        

        res = 0

        for word in words: 
            prev_index = -1
            found = True
        
            for char in word:
                if char not in charMap:
                    found = False
                    break
            

                pos_list = charMap[char]
                new_pos = bisect.bisect_left(pos_list, prev_index + 1)

                if len(pos_list) == new_pos:
                    found = False
                    break
                prev_index = pos_list[new_pos]

            if found:
                res += 1
        return res
