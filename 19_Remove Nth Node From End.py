# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        left = head
        right = head
        for i in range(n):
            right = right.next
        
        if not right:
            head = head.next

        while right and right.next:
            left = left.next
            right = right.next


        if left.next:
            left.next = left.next.next
        else:
            left.next = None

        return head