'''
Given a binary string s, return the minimum number of character swaps to make it alternating, or -1 if it is impossible.

The string is called alternating if no two adjacent characters are equal. For example, the strings "010" and "1010" are alternating, while the string "0100" is not.

Any two characters may be swapped, even if they are not adjacent.

 

Example 1:

Input: s = "111000"
Output: 1
Explanation: Swap positions 1 and 4: "111000" -> "101010"
The string is now alternating.
Example 2:

Input: s = "010"
Output: 0
Explanation: The string is already alternating, no swaps are needed.
Example 3:

Input: s = "1110"
Output: -1
 

Constraints:

1 <= s.length <= 1000
s[i] is either '0' or '1'.
'''
class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)

        count_0  = s.count('0')
        count_1 = s.count('1')

        if abs(count_0 - count_1) > 1:
            return -1

        swap_start_0 = swap_start_1 = 0


        for i, ch in enumerate(s):
            if i % 2 == 0:
                if ch != '0':
                    swap_start_0 +=1
                elif ch != '1':
                    swap_start_1 += 1
            else:
                if ch != '1':
                    swap_start_0 +=1
                elif ch != '0':
                    swap_start_1 +=1
    
        if count_0 > count_1:
            return swap_start_0 // 2
        elif count_1 > count_0:
            return swap_start_1 // 2
        else:
            return min(swap_start_0, swap_start_1) // 2
        

