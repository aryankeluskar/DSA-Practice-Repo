from collections import deque

# dequeue is a double-ended queue, which can pop and push at both ends

deq = deque([1, 2, 3, 4, 5])
print(deq)

# by default, append() adds to the right
deq.append(6)
print(deq)

deq.appendleft(0)
print(deq)

# pop() removes from the right
deq.pop()
print(deq)

deq.popleft()
print(deq)


#               ------------------------------
#               |                            |
#   left <----  |           DEQUE            |  ---> right
#   end         |                            |       end
#               ------------------------------
