'''
Given an integer n representing nodes labeled from 0 to n - 1 in an undirected graph, and an array of non-negative weighted edges, return an array where each index i contains the shortest path length from a specified start node to node i. If a node is unreachable, set its distance to -1.

Each edge is represented by a triplet of positive integers: the start node, the end node, and the weight of the edge.

Example:


Input: n = 6,
       edges = [
         [0, 1, 5],
         [0, 2, 3],
         [1, 2, 1],
         [1, 3, 4],
         [2, 3, 4],
         [2, 4, 5],
       ],
       start = 0
Output: [0, 4, 3, 7, 8, -1]

'''

from typing import List
from collections import defaultdict
import heapq

def shortest_path(n: int, edges: List[int], start: int) -> List[int]:
    # Write your code here
    graph = defaultdict(list)
    for u,v,w in edges:
        graph[u].append((v,w))
        graph[v].append((u,w))

    distances = {i:float('inf') for i in range(n)}
    distances[start] = 0

    heap = [(0,start)]

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance,neighbor))
    
    return [dist if dist != float('inf') else -1 for dist in distances.values()]
