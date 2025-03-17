'''

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3

Output: [1,2,3,4]

Example 2:

Input: arr = [1,1,2,3,4,5], k = 4, x = -1

Output: [1,1,2,3]

 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104

'''
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Step 1: Binary search to find the closest index to x
        pos = bisect.bisect_left(arr, x)
        left, right = pos - 1, pos  # Two pointers
        
        # Step 2: Expand two pointers to find k closest elements
        while k > 0:
            if left < 0:  # No more elements on the left
                right += 1
            elif right >= len(arr):  # No more elements on the right
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):  # Expand left if closer or equal
                left -= 1
            else:  # Expand right if closer
                right += 1
            k -= 1

        # Step 3: Return sorted subarray
        return arr[left + 1:right]
