'''

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

For examples, if arr = [2,3,4], the median is 3.
For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation: 
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6
Example 2:

Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]

'''


#
# @lc app=leetcode id=480 lang=python3
#
# [480] Sliding Window Median
#
import heapq

class HashHeap:
    def __init__(self):
        self.heap = []
        self.deleted = {}       # key (num): value (occurence)
        self._len = 0

    def push(self, val):
        heapq.heappush(self.heap, val)
        self._len += 1

    def pop(self):
        """
        execute lazy removal
        """
        self._clean_top()
        self._len -= 1
        return heapq.heappop(self.heap)

    def remove(self, val):
        self.deleted[val] = self.deleted.get(val, 0) + 1
        self._len -= 1

    def top(self):
        """
        execute lazy removal
        """
        self._clean_top()
        return self.heap[0]

    def _clean_top(self):
        """
        lazy removal
        """
        # if heap top is 
        while self.heap and self.deleted.get(self.heap[0]):
            self.deleted[self.heap[0]] -= 1     # update occurence
            heapq.heappop(self.heap)

    def __len__(self):
        return self._len

    
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        res = [] 
        n = len(nums)
        if not nums or n < 1 or k <= 0: return res
        
        self.min_heap = HashHeap()
        self.max_heap = HashHeap()
        
        for i in range(n):
            # move window
            if i >= k:
                if self.min_heap and nums[i - k] >= self.min_heap.top():
                    self.min_heap.remove(nums[i - k])
                else:
                    self.max_heap.remove(-nums[i - k])
            
            # load the number
            if self.min_heap and nums[i] > self.min_heap.top():
                self.min_heap.push(nums[i])
            else:
                self.max_heap.push(-nums[i])
            
            self.balance()

            if i + 1 >= k:
                res.append(self.get_median(k))        
        
        return res

    def balance(self):
        """
        an important thing to notice is the fact that if the two heaps are balanced, only the top of the 
        heaps are  actually needed to find the medians. This means that as long as we can somehow keep 
        the heaps balanced, we could also keep some extraneous elements.        
        """
        l = len(self.max_heap)
        r = len(self.min_heap)
        if abs(r - l) <= 1: return
        if l < r: self.max_heap.push(-self.min_heap.pop())
        else: self.min_heap.push(-self.max_heap.pop())
        
    def get_median(self, k):
        l = len(self.max_heap)
        r = len(self.min_heap)

        if k % 2 ==0:
            return (-self.max_heap.top() + self.min_heap.top()) / 2.0
        return float(self.min_heap.top() if r > l else -self.max_heap.top())
    
