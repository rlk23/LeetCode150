'''
You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
Example 2:

Input: nums = [1,3,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[3], range = 3 - 3 = 0
[3], range = 3 - 3 = 0
[1,3], range = 3 - 1 = 2
[3,3], range = 3 - 3 = 0
[1,3,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
Example 3:

Input: nums = [4,-2,-3,4,1]
Output: 59
Explanation: The sum of all subarray ranges of nums is 59.
 

Constraints:

1 <= nums.length <= 1000
-109 <= nums[i] <= 109
 

Follow-up: Could you find a solution with O(n) time complexit

'''
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)


        def count_contribution(is_max):
            stack = []
            left = [0] * n
            right = [0] * n
            
            for i in range(n):
                while stack and (nums[stack[-1]] < nums[i] if is_max else nums[stack[-1]] > nums[i]):
                    stack.pop()
                left[i] = i - stack[-1] if stack else i + 1
                stack.append(i)

            stack.clear()

            for i in range(n-1,-1,-1):
                while stack and (nums[stack[-1]] <= nums[i] if is_max else nums[stack[-1]] >= nums[i]):
                    stack.pop()
                right[i] = stack[-1] - i if stack else n - i
                stack.append(i)
            return sum(nums[i] * left[i] * right[i] for i in range(n))

        return count_contribution(True) - count_contribution(False)
