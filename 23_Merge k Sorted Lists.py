from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        # Initialize the head as the first element of the lists
        head = lists[0]

        for i in range(1, len(lists)):
            current_list = lists[i]

            # Helper function to merge two sorted linked lists
            def merge_two_lists(l1, l2):
                dummy = ListNode(0)
                current = dummy

                while l1 and l2:
                    if l1.val < l2.val:
                        current.next = l1
                        l1 = l1.next
                    else:
                        current.next = l2
                        l2 = l2.next
                    current = current.next

                current.next = l1 or l2
                return dummy.next

            # Merge the current list with the existing merged list
            head = merge_two_lists(head, current_list)

        return head

lists = [[1,4,5], [1,3,4], [2,6]]
# Create ListNode objects from the input list
list_nodes = []
for sublist in lists:
    head = ListNode(sublist[0])
    current = head
    for i in range(1, len(sublist)):
        current.next = ListNode(sublist[i])
        current = current.next
    list_nodes.append(head)

s = Solution()
merged_list = s.mergeKLists(list_nodes)

# Print the merged list
while merged_list:
    print(merged_list.val, end=" ")
    merged_list = merged_list.next
