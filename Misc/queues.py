import queue

queueEg = queue.Queue()
queueEg.put(1)
queueEg.put(2)
queueEg.put(3)
queueEg.put(4)
queueEg.put(5)

print("queue rn: " + str(queueEg.queue))
print(queueEg.get())
print(queueEg.get())
print("queue rn: " + str(queueEg.queue))
queueEg.put(int(input("enter a number: ")))
print("queue rn: " + str(queueEg.queue))
print(queueEg.get())
print(queueEg.get())
print("queue rn: " + str(queueEg.queue))


# FIFO - First In First Out
# Stores similar to human lines, ie: append at back and exit from front
# First placed item is first to be removed

# Queue Operations
#       pop
#        Λ
#        |
#        |
#   _____________
#  |    Top      |
#  |             |
#  |             |
#  |             |
#  |             |
#  |             |
#  |             |
#  |             |
#  |   Queue     |
#  |             |
#  |             |
#  |             |
#  |             |
#  |   Bottom    |
#  |_____________|
#        Λ
#        |
#        |
#       push
