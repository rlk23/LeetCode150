'''

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def quick_select(start, end, k_smallest):
            # If the list contains only one element,
            # return that element
            if start == end:
                return nums[start]
            pivot_index = (start + end) // 2  # Choose the middle element as the pivot
            pivot_value = nums[pivot_index]
            left, right = start - 1, end + 1
          
            # Partition the list such that all elements greater than
            # the pivot are to the left and all elements less than
            # are to the right
            while left < right:
                # Increment left index until finding an element less than the pivot
                while True:
                    left += 1
                    if nums[left] >= pivot_value:
                        break
                # Decrement right index until finding an element greater than the pivot
                while True:
                    right -= 1
                    if nums[right] <= pivot_value:
                        break
                # Swap elements from both sides if needed
                if left < right:
                    nums[left], nums[right] = nums[right], nums[left]
          
            # If the partitioning index is less than k_smallest, we know that
            # the kth largest element must be in the right partition.
            # If it's greater than or equal to k_smallest, the element will
            # be in the left partition.
            if right < k_smallest:
                return quick_select(right + 1, end, k_smallest)
            return quick_select(start, right, k_smallest)

        # Calculate the 'k_smallest' index based on the 'kth largest' requirement
        n = len(nums)
        k_smallest = n - k
        # Call the quick_select helper function to find the kth largest element
        return quick_select(0, n - 1, k_smallest)

