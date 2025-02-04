'''
Return the kth largest integer in an array.

Example:
Input: nums = [5, 2, 4, 3, 1, 6], k = 3
Output: 4
Constraints:
The array contains no duplicates.
The array contains at least one element.
1 ≤ k ≤ n, where n denotes the length of the array.
'''

from typing import List

def quick_sort(nums):
    if len(nums) == 0:
        return []

    pivot = nums[0]
    left = [x for x in nums[1:] if x < pivot]
    right = [x for x in nums[1:] if x >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

def kth_largest_integer(nums: List[int], k: int) -> int:
    # Write your code here
    res = quick_sort(nums)
    n = len(nums)


    return res[n - k]
