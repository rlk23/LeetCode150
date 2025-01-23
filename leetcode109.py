'''
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

'''

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Base case: if the list is empty
        if not head:
            return None
        
        # If only one node, create a tree with that node
        if not head.next:
            return TreeNode(head.val)
        
        # Find the middle of the linked list
        prev = None
        slow = fast = head
        
        # Move slow pointer to middle, fast pointer to end
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        # Disconnect the left half from the middle
        prev.next = None
        
        # Create root with middle value
        root = TreeNode(slow.val)
        
        # Recursively construct left and right subtrees
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        
        return root
