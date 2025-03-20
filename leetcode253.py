'''
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
 

Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106

'''

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0

        min_heap = []

        intervals.sort(key=lambda x:x[0])

        heapq.heappush(min_heap, intervals[0][1])

        for start, end in intervals[1:]:
            if start >= min_heap[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, end)
        return len(min_heap)
