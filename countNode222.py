'''
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Function to compute the depth of the leftmost path
        def compute_depth(node):
            depth = 0
            while node:
                depth += 1
                node = node.left
            return depth

        left_depth = compute_depth(root.left)
        right_depth = compute_depth(root.right)

        if left_depth == right_depth:
            # Left subtree is a perfect binary tree
            return (1 << left_depth) + self.countNodes(root.right)
        else:
            # Right subtree is a perfect binary tree
            return (1 << right_depth) + self.countNodes(root.left)