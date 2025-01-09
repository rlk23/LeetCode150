'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

'''


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumulative_sum_counter = Counter({0:1})

        count_subarrays = 0
        count_sum = 0


        for num in nums:
            count_sum += num

            count_subarrays += cumulative_sum_counter[count_sum - k]

            cumulative_sum_counter[count_sum] += 1
        return count_subarrays
