"""
URL: https://leetcode.com/problems/merge-k-sorted-lists/

"""
from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0 or not lists:
            return
        while len(lists) > 1:
            merged_list = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_list.append(self.mergeList(list1, list2))
            lists = merged_list
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            v1 = l1.val
            v2 = l2.val

            if v1 < v2:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2

        return dummy.next


"""
Runtime
78 ms Beats 59.01% of users with Python3
Memory
19.33 MB Beats 73.72% of users with Python3
"""