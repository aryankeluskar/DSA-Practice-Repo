# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(0)
        curr = res

        while True:
            min_found = -1

            for index in range(len(lists)):
                if lists[index] is None:
                    continue

                if min_found == -1 or lists[index].val < lists[min_found].val:
                    min_found = index

            # print(min_found)

            if min_found == -1:
                break

            curr.next = ListNode(lists[min_found].val)
            curr = curr.next
            lists[min_found] = lists[min_found].next

        return res.next