'''
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:


Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
 

Constraints:

2 <= n <= 105
n - 1 <= connections.length <= 105
0 <= ai, bi <= n - 1
ai != bi
There are no repeated connections.
'''
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = {i:[] for i in range(n)}

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        # Step 2: Initialize Data Structures
        discovery = [-1] * n  # Discovery time of each node
        low = [-1] * n        # Lowest discovery time reachable
        time = 0
        bridges = []


        def dfs(node, parent):
            nonlocal time
            discovery[node] = low[node] = time
            time += 1

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue  # Skip the edge leading to the parent
                
                if discovery[neighbor] == -1:  # If neighbor not visited
                    dfs(neighbor, node)
                    low[node] = min(low[node], low[neighbor])  # Update low-link value

                    # Condition for a bridge
                    if low[neighbor] > discovery[node]:
                        bridges.append([node, neighbor])

                else:  # If already visited, update low-link value
                    low[node] = min(low[node], discovery[neighbor])

        # Step 3: Run DFS from any node (0)
        for i in range(n):
            if discovery[i] == -1:
                dfs(i, -1)

        return bridges

