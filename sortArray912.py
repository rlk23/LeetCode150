'''
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.
 

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104

'''

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):
            # Base case: Single element is already sorted
            if len(arr) <= 1:
                return arr
            
            # Split the array into two halves
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            # Merge the two sorted halves
            return merge(left, right)
        
        def merge(left, right):
            sorted_array = []
            i = j = 0
            
            # Merge two sorted arrays
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    sorted_array.append(left[i])
                    i += 1
                else:
                    sorted_array.append(right[j])
                    j += 1
            
            # Append remaining elements from left array
            while i < len(left):
                sorted_array.append(left[i])
                i += 1
            
            # Append remaining elements from right array
            while j < len(right):
                sorted_array.append(right[j])
                j += 1
            
            return sorted_array
        
        # Call merge_sort on the input nums
        return merge_sort(nums)
