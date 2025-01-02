# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False

        if head.next == None:
            return False
        

        slow, fast = head, head.next

        while slow and fast:
            if slow == fast:
                return True

            slow = slow.next

            if fast.next:
                fast = fast.next.next
            else:
                return False

        return False