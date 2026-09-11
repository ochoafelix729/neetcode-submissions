import random

class RandomizedSet:

    def __init__(self):
        self.indices = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val not in self.indices:
            self.data.append(val)
            self.indices[val] = len(self.data) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.indices:
            tail = self.indices[val]
            tail_val = self.data[-1]
            self.data[-1], self.data[tail] = self.data[tail], self.data[-1]
            self.indices[tail_val] = self.indices[val]
            del self.indices[val]
            self.data.pop()
            return True
        return False

    def getRandom(self) -> int:
        return self.data[random.randint(0, len(self.data) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()