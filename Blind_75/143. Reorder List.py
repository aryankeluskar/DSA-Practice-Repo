# Definition for singly-linked list.
import math
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp = head.next

        nodes = []
        while temp:
            nodes.append(temp)
            temp = temp.next

        nodes = nodes[ math.ceil(len(nodes)/2): ]

        for i in nodes:
            print(i.val)

        temp = head
        
        i = 0
        while temp and i < len(nodes):
            print("val: ", temp.val)

            curr_next = temp.next
            temp.next = nodes[i]
            nodes[i].next = curr_next
            temp = curr_next

            i += 1

        temp.next.next = None

# Create the linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

# Create solution object and test
solution = Solution()
solution.reorderList(head)

# Print result
curr = head
while curr:
    print("after val", curr.val)
    curr = curr.next

