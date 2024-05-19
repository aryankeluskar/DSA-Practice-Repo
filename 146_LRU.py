from collections import deque


class LRUCache:
    def __init__(self, capacity: int):
        self.map = {}
        self.c = 0
        self.cap = capacity
        self.q = deque()

    def get(self, key: int) -> int:
        if not key in self.q:
            return -1
        # self.q.remove(key)
        # self.q.append(key)
        self.q.remove(key)
        self.q.appendleft(key)
        return self.map[key]

    def put(self, key: int, value: int) -> None:
        if not key in self.q:
            self.c += 1
            self.map[key] = value
            self.q.appendleft(key)

        if key in self.q:
            self.q.remove(key)
            self.q.appendleft(key)
            self.map[key] = value

        if self.c > self.cap:
            evic = self.q.pop()
            # print(evic)
            # print(self.map)
            
            self.c -= 1
            pass            
        

    def strr(self):
        return str(self.map)


lru = LRUCache(2)
lru.put(2, 1)
lru.put(2, 2)
print(lru.get(2))
lru.put(1, 1)
lru.put(4, 1)
print(lru.strr())
# print(lru.get(1))