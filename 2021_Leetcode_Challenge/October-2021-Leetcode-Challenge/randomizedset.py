class RandomizedSet:

    def __init__(self):
        self.items = []

    def insert(self, val: int) -> bool:
        if val not in self.items:
            self.items.append(val)
            return False
        else:
            return True

    def remove(self, val: int) -> bool:
        if val in self.items:
            self.items.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        import random
        return random.choice(self.items)


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_3 = obj.getRandom()


["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]

print(param_1, param_2, param_3)
