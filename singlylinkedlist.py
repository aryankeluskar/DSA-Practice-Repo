# LinkedList!!!
# does not store data continuously, allows for dynamic memory allocation and flexibility
# Following is a singly linked list, ie: each node has a value and a pointer to the next node


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


blue = ListNode("blue")
red = ListNode("red")
green = ListNode("green")

blue.next = red
red.next = green

print(blue.val)
print(blue.next.val)

# Traverse a linked list:
curr = blue
while curr:
    print(curr.val)
    curr = curr.next

# Appending at the end:
newVal = input("Enter the value you want to append: ")
newNode = ListNode(newVal)
curr = blue
while curr.next:
   curr = curr.next
curr.next = newNode

# Appending at beginning
newVal = input("Enter the value you want to start: ")
newNode = ListNode(newVal)
newNode.next = blue
curr = newNode

# Traverse a linked list again:
while curr:
    print(curr.val)
    curr = curr.next