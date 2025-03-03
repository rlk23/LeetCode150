'''
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.

'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        count = 0

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()

                if stack:
                    count = max(count, i - stack[-1])
                else:
                    stack.append(i)
        return count
