'''
There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.

Return a sorted list of the items such that:

The items that belong to the same group are next to each other in the sorted list.
There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).
Return any solution if there is more than one solution and return an empty list if there is no solution.

 

Example 1:



Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
Output: [6,3,4,1,5,2,0,7]
Example 2:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
Output: []
Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.
 

Constraints:

1 <= m <= n <= 3 * 104
group.length == beforeItems.length == n
-1 <= group[i] <= m - 1
0 <= beforeItems[i].length <= n - 1
0 <= beforeItems[i][j] <= n - 1
i != beforeItems[i][j]
beforeItems[i] does not contain duplicates elements.
'''
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        for i in range(len(group)):
            if group[i] == -1:
                group[i] = m
                m += 1
        
        item_graph = collections.defaultdict(list)
        item_degree = [0]* n


        group_graph = collections.defaultdict(list)
        group_degree = [0] * m


        for i in range(n):
            for pre in beforeItems[i]:
                item_graph[pre].append(i)
                item_degree[i] += 1

                if group[i] != group[pre]:
                    group_graph[group[pre]].append(group[i])
                    group_degree[group[i]] += 1


        def topological_sort(graph, in_degree, nodes):
            queue = deque([node for node in nodes if in_degree[node] == 0])
            sorted_order = []

            while queue:
                node = queue.popleft()
                sorted_order.append(node)

                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

            return sorted_order if len(sorted_order) == len(nodes) else [] 

        sorted_items = topological_sort(item_graph, item_degree, range(n))

        if not sorted_items:
            return []
        
        grouped_items = collections.defaultdict(list)
        for item in sorted_items:
            grouped_items[group[item]].append(item)

        sorted_groups = topological_sort(group_graph, group_degree, range(m))
        if not sorted_groups:
            return []

        result = []
        for group_id in sorted_groups:
            result.extend(grouped_items[group_id])

        return result
        
