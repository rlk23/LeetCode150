'''
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1
 

 

Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 105
All the values of routes[i] are unique.
sum(routes[i].length) <= 105
0 <= routes[i][j] < 106
0 <= source, target < 106


'''
from collections import deque, defaultdict
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0  # No buses needed if source is the same as target

        # Step 1: Build a graph where nodes are routes
        stop_to_routes = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(i)

        # Step 2: BFS to find the minimum number of buses
        queue = deque([(source, 0)])  # (current stop, buses taken)
        visited_stops = set()  # Visited stops
        visited_routes = set()  # Visited routes

        while queue:
            current_stop, buses = queue.popleft()

            # Check if we've reached the target
            if current_stop == target:
                return buses

            # Visit all routes passing through the current stop
            for route in stop_to_routes[current_stop]:
                if route in visited_routes:
                    continue  # Skip already visited routes
                visited_routes.add(route)

                # Add all stops in this route to the queue
                for stop in routes[route]:
                    if stop not in visited_stops:
                        visited_stops.add(stop)
                        queue.append((stop, buses + 1))

        return -1  # If target is unreachable


