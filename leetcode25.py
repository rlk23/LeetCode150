'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 

Follow-up: Can you solve the problem in O(1) extra memory space?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or k == 1:
            return head
        curr = head

        length = 0

        while curr:
            length += 1
            curr = curr.next

        dummy  = ListNode(0,head)
        prev_group_end = dummy
 

        while length >= k:
            prev, curr = None, prev_group_end.next
            group_head = curr
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            
            prev_group_end.next = prev  # prev is the new head of this segment
            group_head.next = curr  # Connect to the next part of the list
            
            # Move prev_group_end forward to the end of the reversed group
            prev_group_end = group_head
            length -= k 

        return dummy.next


        
