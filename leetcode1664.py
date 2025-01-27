'''
You are given an integer array nums. You can choose exactly one index (0-indexed) and remove the element. Notice that the index of the elements may change after the removal.

For example, if nums = [6,1,7,4,1]:

Choosing to remove index 1 results in nums = [6,7,4,1].
Choosing to remove index 2 results in nums = [6,1,4,1].
Choosing to remove index 4 results in nums = [6,1,7,4].
An array is fair if the sum of the odd-indexed values equals the sum of the even-indexed values.

Return the number of indices that you could choose such that after the removal, nums is fair.

 

Example 1:

Input: nums = [2,1,6,4]
Output: 1
Explanation:
Remove index 0: [1,6,4] -> Even sum: 1 + 4 = 5. Odd sum: 6. Not fair.
Remove index 1: [2,6,4] -> Even sum: 2 + 4 = 6. Odd sum: 6. Fair.
Remove index 2: [2,1,4] -> Even sum: 2 + 4 = 6. Odd sum: 1. Not fair.
Remove index 3: [2,1,6] -> Even sum: 2 + 6 = 8. Odd sum: 1. Not fair.
There is 1 index that you can remove to make nums fair.
Example 2:

Input: nums = [1,1,1]
Output: 3
Explanation: You can remove any index and the remaining array is fair.
Example 3:

Input: nums = [1,2,3]
Output: 0
Explanation: You cannot make a fair array after removing any index.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104

'''

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        even_prefix = [0] * n
        odd_prefix = [0] * n

        for i in range(n):

            if i == 0:
                even_prefix[i] = nums[i] if i % 2 == 0 else 0
                odd_prefix[i] = nums[i] if i % 2 != 0 else 0
            else:
                even_prefix[i] = even_prefix[i - 1] + (nums[i] if i % 2 == 0 else 0)
                odd_prefix[i] = odd_prefix[i - 1] + (nums[i] if i % 2 != 0 else 0)
        fair_count = 0

        for i in range(n):
            # Calculate sums after removing nums[i]
            even_sum = (even_prefix[i - 1] if i > 0 else 0) + (odd_prefix[n - 1] - odd_prefix[i])
            odd_sum = (odd_prefix[i - 1] if i > 0 else 0) + (even_prefix[n - 1] - even_prefix[i])

            # Check if the sums are equal
            if even_sum == odd_sum:
                fair_count += 1

        return fair_count
