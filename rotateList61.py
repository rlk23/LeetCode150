'''
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
      
        # Count the number of elements in the linked list
        current, length = head, 0
        while current:
            length += 1
            current = current.next

        # Compute the actual number of rotations needed as k could be larger than the length of the list
        k %= length
        if k == 0:  # If no rotation is needed
            return head

        # Use two pointers, fast and slow. Start both at the beginning of the list
        fast = slow = head
      
        # Move the fast pointer k steps ahead
        for _ in range(k):
            fast = fast.next
      
        # Move both pointers at the same speed until fast reaches the end of the list
        while fast.next:
            fast, slow = fast.next, slow.next
      
        # At this point, slow is at the node before the new head after rotation
        # We can now adjust the pointers to complete the rotation
        new_head = slow.next
        slow.next = None  # The next pointer of the new tail should point to None
        fast.next = head  # The next pointer of the old tail should point to the old head
      
        return new_head  # Return the new head of the list
