'''
Given two strings s and p, return an array of all the start indices of p's 
anagrams
 in s. You may return the answer in any order.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.

'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s = len(s)
        len_p = len(p)

        if len_p > len_s:
            return []

        res = []

        p_count = Counter(p)

        window_counter = Counter()

        for i in range(len_p):
            window_counter[s[i]] += 1
        
        if window_counter == p_count:
            res.append(0)
        

        for i in range(len_p, len_s):

            window_counter[s[i]] += 1

            window_counter[s[i-len_p]] -= 1


            if window_counter[s[i-len_p]] == 0:
                del window_counter[s[i-len_p]]
            
            if window_counter == p_count:
                start_index = i - len_p + 1
                res.append(start_index)


        return res
