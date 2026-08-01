class MyHashMap:

    def __init__(self):
        self.hashmap = [[] for _ in range(10000)]
        self.keys = set()
        
    def hash(self, key: int) -> int:
        return key % len(self.hashmap)
        

    def put(self, key: int, value: int) -> None:
        print(key, value)
        idx = self.hash(key)
        if key in self.keys:
            i = 0
            while i < len(self.hashmap[idx]):
                if self.hashmap[idx][i][0] == key:
                    self.hashmap[idx][i][1] = value
                    print(self.hashmap[idx])
                    return
                i += 1
        self.keys.add(key)
        self.hashmap[idx].append([key,value])
        print(self.hashmap[idx])

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        idx = self.hash(key)
        for k, v in self.hashmap[idx]:
            if k == key:
                return v

    def remove(self, key: int) -> None:
        if key not in self.keys:
            return
        idx = self.hash(key)
        for k, v in self.hashmap[idx]:
            if k == key:
                self.hashmap[idx].remove([k,v])
                self.keys.remove(key)
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)