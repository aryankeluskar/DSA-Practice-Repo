import queue


class MyStack:
    def __init__(self):
        self.arr = queue.Queue()

    def push(self, x: int) -> None:
        self.arr.put(x)
        for _ in range(self.arr.qsize() - 1):
            self.arr.put(self.arr.get())

    # Push Works like:
    # deque([10, 11, 12, 13, 14])
    # deque([11, 12, 13, 14, 10])
    # deque([12, 13, 14, 10, 11])
    # deque([13, 14, 10, 11, 12])
    # deque([14, 10, 11, 12, 13])

    #   print(str(self.arr.queue))

    def pop(self) -> int:
        # print(str(self.arr.queue))
        return self.arr.get()

    def top(self) -> int:
        return self.arr.queue[0]

    def empty(self) -> bool:
        return self.arr.empty()
