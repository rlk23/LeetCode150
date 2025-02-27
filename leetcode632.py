'''
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

 

Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Example 2:

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]
 

Constraints:

nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-105 <= nums[i][j] <= 105
nums[i] is sorted in non-decreasing order.

'''
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []

        max_val = float('-inf')

        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0],i,0))
            max_val = max(max_val, nums[i][0])
        
        best_range = [float('-inf'), float('inf')]


        while min_heap:
            min_val, list_index, element_index = heapq.heappop(min_heap)

        
            if max_val - min_val < best_range[1] - best_range[0]:
                best_range = [min_val, max_val]

            if element_index + 1 < len(nums[list_index]):
                next_val = nums[list_index][element_index+1]
                heapq.heappush(min_heap, (next_val, list_index, element_index+ 1))
                max_val = max(next_val, max_val)
            else:
                break
            

            

        return best_range
