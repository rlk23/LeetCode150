'''
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
 

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
'''
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = {char:i for i, char in enumerate(s)}

        seen = set()
        stack = []

        for i, c in enumerate(s):
            if c in seen:
                continue
            
            while stack and c < stack[-1] and  last_index[stack[-1]] > i:
                seen.remove(stack.pop())

            stack.append(c)
            seen.add(c)
        return "".join(stack)
