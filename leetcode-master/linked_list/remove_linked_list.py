

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        curr = head
        prev = dummy
        prev.next = curr
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next

"""
Runtime
50 ms Beats 48.54% of users with Python3
Memory
19.32 MB Beats 85.67% of users with Python3
"""