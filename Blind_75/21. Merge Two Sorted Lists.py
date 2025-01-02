# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None:
            return list2

        if list2 == None:
            return list1
        
        if list1.val > list2.val:
            final = list2
            list2 = list2.next
        else:
            final = list1
            list1 = list1.next

        head = final

        one = list1
        two = list2

        while one and two:
            if one.val > two.val:
                final.next = two
                two = two.next
                final = final.next
            else:
                final.next = one
                one = one.next
                final = final.next

        while one:
            final.next = one
            one = one.next
            final = final.next

        while two:
            final.next = two
            two = two.next
            final = final.next

        return head