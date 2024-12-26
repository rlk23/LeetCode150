'''
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
'''

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        current_number = 0
        stack = []
        last_ops = "+"


        for i, c in enumerate(s):
            if c.isdigit():
                current_number = current_number * 10 + int(c)

            if not c.isdigit() or i == len(s) - 1:
                if last_ops == "+":
                    stack.append(current_number)
                elif last_ops == "-":
                    stack.append(-current_number)
                elif last_ops == "*":
                    stack[-1] *= current_number
                elif last_ops == "/":
                    stack[-1] = int(stack[-1] / current_number)

                
                last_ops = c
                current_number = 0

        return sum(stack)
