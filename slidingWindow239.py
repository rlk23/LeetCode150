'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 




'''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        queue = collections.deque()

        res = []
        i = 0
        while i < len(nums):
            # Remove indices that are out of the current window
            if queue and queue[0] < i - k + 1:
                queue.popleft()
            
            # Remove indices of smaller elements, as they won't be needed
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            # Append the current index
            queue.append(i)

            # Append the maximum for the current window
            if i >= k - 1:
                res.append(nums[queue[0]])
            
            i += 1

        return res
