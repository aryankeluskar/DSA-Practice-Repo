class ListNode:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistory:
    def __init__(self, homepage: str):
        site = ListNode(val=homepage)
        self.curr = site
        print(self.curr.val)

    def visit(self, url: str) -> None:
        newSite = ListNode(val=url, prev=self.curr, next=None)
        print(newSite.prev.val, newSite.next, newSite.val)
        self.curr.next = newSite
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        #   try:
        temp = self.curr
        print("called prev on " + self.curr.val)
        for _ in range(steps):
            if temp.prev == None:
                break
            temp = temp.prev
        print("done with next on " + temp.val)
        self.curr = temp
        return temp.val

    def forward(self, steps: int) -> str:
        #   try:
        temp = self.curr
        print("called next on " + self.curr.val)
        for _ in range(steps):
            if temp.next == None:
                break
            temp = temp.next
        self.curr = temp
        print("done with next on " + temp.val)
        return temp.val

    #   except:
    #       return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
