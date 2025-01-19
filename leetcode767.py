'''

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
'''

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        maxHeap = []

        for char, count in freq.items():
            heapq.heappush(maxHeap,(-count,char))

        prev_char, prev_count = None,0
        result = []

        while maxHeap:
            count,char = heapq.heappop(maxHeap)
            result.append(char)

            if prev_count < 0:
                heapq.heappush(maxHeap,(prev_count,prev_char))

            prev_char = char
            prev_count = count + 1


        result_str = "".join(result)
        if len(result_str) != len(s):
            return ""
        return result_str
