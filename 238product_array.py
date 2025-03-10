'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        l_arr = [0] * n
        r_arr = [0] * n

        l_mult = 1
        r_mult = 1

        for i in range(len(nums)):
            j = -i -1

            l_arr[i] = l_mult
            r_arr[j] = r_mult

            l_mult *= nums[i]
            r_mult *= nums[j]

        return [l*r for l,r in zip(l_arr,r_arr)]
