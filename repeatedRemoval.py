'''
Given a string, continually perform the following operation: remove a pair of adjacent duplicates from the string. Continue performing this operation until the string no longer contains pairs of adjacent duplicates. Return the final string.

Example 1:


Input: s = 'aacabba'
Output: 'c'
Example 2:


Input: s = 'aaa'
Output: 'a'
'''

def repeated_removal_of_adjacent_duplicates(s: str) -> str:
    # Write your code here
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)
