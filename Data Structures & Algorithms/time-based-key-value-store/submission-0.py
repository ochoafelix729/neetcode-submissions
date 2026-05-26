from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list) # str : [[timestamp, value]]

    # O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([timestamp, value])
        
    # O(log n)
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        l, r = 0, len(self.hashmap[key])-1
        while l <= r:
            mid = (l+r) // 2

            if timestamp < self.hashmap[key][mid][0]:
                r = mid-1
            else:
                res = self.hashmap[key][mid][1]
                print(res)
                l = mid+1
        return res

