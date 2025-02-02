'''
Given a string representing a mathematical expression containing integers, parentheses, addition, and subtraction operators, evaluate and return the result of the expression.

Example:
Input: s = '18-(7+(2-4))'
Output: 13
'''

def evaluate_expression(s: str) -> int:
    stack = []
    res = 0  # Stores the running sum of current expression
    sign = 1  # 1 for '+' and -1 for '-'
    num = 0  # Stores the current number

    for i, char in enumerate(s):
        if char.isdigit():
            num = num * 10 + int(char)  # Form multi-digit numbers
        
        if char in "+-(" or i == len(s) - 1 or char == ")":
            # Process the number before handling operators
            res += sign * num
            num = 0  # Reset number

            if char == "-":
                sign = -1
            elif char == "+":
                sign = 1
            elif char == "(":
                stack.append(res)  # Store current result
                stack.append(sign)  # Store current sign
                res, sign = 0, 1  # Reset result and sign for sub-expression
            elif char == ")":
                res *= stack.pop()  # Apply sign before '('
                res += stack.pop()  # Add result before '('

    return res


