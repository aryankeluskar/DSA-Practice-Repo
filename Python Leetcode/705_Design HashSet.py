class MyHashSet:
    def __init__(self):
        self.contain_set = {}

    def add(self, key: int) -> None:
        self.contain_set[key] = True

    def remove(self, key: int) -> None:
        self.contain_set[key] = False

    def contains(self, key: int) -> bool:
        return self.contain_set[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
