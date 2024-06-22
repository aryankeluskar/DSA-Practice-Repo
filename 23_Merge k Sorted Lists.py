# Python program to merge k sorted listsays of size n each

# A Linked List node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


from queue import PriorityQueue


# Function to merge K sorted linked lists
def mergeKLists(lists):
    # Create a priority queue
    pq = PriorityQueue()

    # Push the first elements of all linked lists into the priority queue
    for i in range(len(lists)):
        if lists[i] is not None:
            pq.put((lists[i].data, i))

    head = Node(None)
    curr = head

    # Merge the linked lists
    while not pq.empty():
        val, i = pq.get()
        curr.next = Node(val)
        curr = curr.next
        if lists[i].next is not None:
            pq.put((lists[i].next.data, i))
            lists[i] = lists[i].next

    return head.next


# Function to print nodes in a given linked list
def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()


# Driver program to test the functions
if __name__ == "__main__":
    k = 3  # Number of linked lists
    n = 4  # Number of elements in each list

    # An listsay of pointers storing the head nodes
    # of the linked lists
    lists = [None] * k

    lists[0] = Node(1)
    lists[0].next = Node(3)
    lists[0].next.next = Node(5)
    lists[0].next.next.next = Node(7)

    lists[1] = Node(2)
    lists[1].next = Node(4)
    lists[1].next.next = Node(6)
    lists[1].next.next.next = Node(8)

    lists[2] = Node(0)
    lists[2].next = Node(9)
    lists[2].next.next = Node(10)
    lists[2].next.next.next = Node(11)

    head = mergeKLists(lists, k)

    print("Merged Linked List:")
    printList(head)

# This code is contributed by shivamgupta310570
