from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        curr1, curr2 = list1, list2
        head = ListNode()
        curr = head
        while curr1 and curr2:
            if curr2.val > curr1.val:
                curr.next = curr1
                curr1 = curr1.next

            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next

        curr.next = curr1 or curr2

        return head.next