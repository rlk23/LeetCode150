'''

Code


Testcase
Test Result
Test Result
109. Convert Sorted List to Binary Search Tree
Solved
Medium
Topics
Companies
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a 
height-balanced
 binary search tree.

 

Example 1:


Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:

Input: head = []
Output: []
 

Constraints:

The number of nodes in head is in the range [0, 2 * 104].
-105 <= Node.val <= 105

'''


"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def isUniform(r1,c1,r2,c2):
            val = grid[r1][c1]
            for r in range(r1,r2+1):
                for c in range(c1,c2+1):
                    if grid[r][c] != val:
                        return False, val
            return True, val

        

        def build(r1, c1, r2,c2):
            uniform, val = isUniform(r1,c1,r2,c2)

            if uniform:
                return Node(val == 1, True)

            midRow = (r1+r2) // 2
            midCol = (c1+c2) // 2
            
            return Node(
                val=True,  # Can be True/False since it's not a leaf
                isLeaf=False,
                topLeft=build(r1, c1, midRow, midCol),
                topRight=build(r1, midCol + 1, midRow, c2),
                bottomLeft=build(midRow + 1, c1, r2, midCol),
                bottomRight=build(midRow + 1, midCol + 1, r2, c2)
            )
        
        return build(0,0,len(grid)-1, len(grid[0])-1)
