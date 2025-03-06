'''

Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
 

Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1
Example 2:

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0
 

Constraints:

2 <= timePoints.length <= 2 * 104
timePoints[i] is in the format "HH:MM".

'''
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        for time in timePoints:
            totalTime = 0
            hr = time[0] + time[1]
            minutes = time[3] + time[4]

            totalTime  = int(hr) * 60 + int(minutes)
        
            times.append(totalTime)
        

        times.sort()
        
        minDiff = float('inf')
        for i in range(1, len(times)):
            minDiff = min(minDiff, times[i] - times[i-1])

        wrapDiff = (times[0] + 1440) - times[-1]
        minDiff = min(wrapDiff, minDiff)
        return minDiff

