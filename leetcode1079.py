'''
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1
 

Constraints:

1 <= tiles.length <= 7
tiles consists of uppercase English l

'''

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(counter):

            total_sequence = 0

            for char in counter:
                if counter[char] > 0:
                    total_sequence += 1

                    counter[char] -= 1
                    total_sequence += backtrack(counter)
                    counter[char] += 1
            return total_sequence


        counter = Counter(tiles)
        return backtrack(counter)
