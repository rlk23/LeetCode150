'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109

'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Helper function to calculate the total hours needed at speed k
        def calculate_time(k):
            total_time = 0
            for pile in piles:
                total_time += (pile + k - 1) // k  # Equivalent to ceil(pile / k)
            return total_time

        # Binary search bounds
        left, right = 1, max(piles)
        result = right

        while left <= right:
            mid = (left + right) // 2  # Current candidate for k
            if calculate_time(mid) <= h:
                result = mid  # Update result, as mid is a valid speed
                right = mid - 1  # Try smaller speeds
            else:
                left = mid + 1  # Try larger speeds

        return result
