'''

Widest Binary Tree Level
Medium
Return the width of the widest level in a binary tree, where the width of a level is defined as the distance between its leftmost and rightmost non-null nodes.

Example:
'''
from ds import TreeNode
from collections import deque

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
"""

def widest_binary_tree_level(root: TreeNode) -> int:
    # Write your code here
    
    if not root:
        return 0
    queue = deque([(root, 0)])  # (node, position index)

    max_width = 0

    while queue:
        level_size = len(queue)
        _ , left_index = queue[0]
        _ , right_index = queue[-1]

        max_width = max(max_width, right_index - left_index + 1)

        for i in range(len(queue)):
            node, index = queue.popleft()

            if node.left:
                queue.append((node.left, 2 * index))
            if node.right:
                queue.append((node.right, 2 * index + 1))
    return max_width
