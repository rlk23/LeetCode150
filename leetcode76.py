'''
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return ""

        
        count_t = Counter(t)

        window = Counter()

        min_length = float("inf")
        min_window = ""

        required_chars = len(count_t)  # Unique chars in t
        formed_chars = 0  # Unique chars satisfied in current window

        l = 0

        for r in range(len(s)):
            window[s[r]] += 1

            if s[r] in count_t and window[s[r]] == count_t[s[r]]:
                formed_chars += 1

            while formed_chars == required_chars:
                if r - l + 1 < min_length:
                    min_length = r-l + 1
                    min_window = s[l: r+1]


                window[s[l]] -= 1

                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    formed_chars -= 1
                
                l += 1
        return min_window
