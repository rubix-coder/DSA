from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # iterative
        n, curr = 0, head
        while curr: n, curr = n + 1, curr.next

        # recursive
        def length(head: ListNode):
            return 0 if not head else 1 + length(head.next)
