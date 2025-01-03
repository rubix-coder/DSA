"""
URL: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.



Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]


Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        if head == None or head.next == None:
            return head

        while curr and curr.next:

            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head


"""
Runtime
50
ms
Beats
5.64%
of users with Python3
Memory
16.42
MB
Beats
94.67%
of users with Python3
"""