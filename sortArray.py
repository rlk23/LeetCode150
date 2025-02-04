'''
Given an integer array, sort the array in ascending order.

Example:
Input: nums = [6, 8, 4, 2, 7, 3, 1, 5]
Output: [1, 2, 3, 4, 5, 6, 7, 8]

'''


from typing import List

def merge(left, right):
    sorted_list = []

    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1

        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

def sort_array(nums: List[int]) -> List[int]:
    # Write your code here
    if len(nums) <= 1:
        return nums  # Base case: already sorted

    mid = len(nums) // 2

    left = sort_array(nums[:mid])
    right = sort_array(nums[mid:])

    return merge(left, right)
