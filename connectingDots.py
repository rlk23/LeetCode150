'''
Connect the Dots
Medium
Given a set of points on a plane, determine the minimum cost to connect all these points.

The cost of connecting two points is equal to the Manhattan distance between them, which is calculated as |x1 - x2| + |y1 - y2| for two points (x1, y1) and (x2, y2).

Example:


Input: points = [[1, 1], [2, 6], [3, 2], [4, 3], [7, 1]]
Output: 15
Constraints:
There will be at least 2 points on the plane.

'''

from typing import List
import heapq

def connect_the_dots(points: List[List[int]]) -> int:
    # Write your code here
    n = len(points)
    heap = [(0,0)]
    visit = set()
    total_cost = 0

    while len(visit) < n:
        cost, point = heapq.heappop(heap)

        if point in visit:
            continue

        total_cost += cost
        visit.add(point)

        for next_point in range(n):
            x1,y1 = points[point]
            x2,y2 = points[next_point]

            man_dis = abs(x1-x2) + abs(y1-y2)
            heapq.heappush(heap, (man_dis,next_point))
    return total_cost
