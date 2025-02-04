'''


'''

from ds import ListNode

def merge(left, right):

    dummy = ListNode()
    tail = dummy

    while left and right:
        if left.val < right.val:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next
    tail.next = left if left else right
    return dummy.next


def sort_linked_list(head: ListNode) -> ListNode:
    # Write your code here
    if not head or not head.next:
        return head

    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    mid = slow.next
    slow.next = None

    left =sort_linked_list(head)
    right = sort_linked_list(mid)
    return merge(left,right)
