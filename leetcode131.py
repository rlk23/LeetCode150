'''
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 
'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_palindrome( s):
            return s == s[::-1]
        

        def backtrack(i, path):
            if i == len(s):
                result.append(path[:])
                return 
            
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(j+1, path)
                    path.pop()
    
        backtrack(0,[])
        return result
