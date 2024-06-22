class MinStack:
    stack = []

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        last = self.stack[-1]
        self.stack.pop()
        return last

    def top(self) -> int:
        print(self.stack)
        return self.stack[0]

    def getMin(self) -> int:
        minEle = self.stack[0]
        for i in self.stack:
            if i < minEle:
                minEle = i
        return minEle


# Your Minself.stack object will be instantiated and called as such:
# obj = Minstack()
# obj.push(2)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
