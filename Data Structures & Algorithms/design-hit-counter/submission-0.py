class HitCounter:

    def __init__(self):
        self.timestamps = []
        self.timestamp_map = {}
        self.left = 0

    def hit(self, timestamp: int) -> None:
        self.timestamps.append(timestamp)
        self.timestamp_map[timestamp] = len(self.timestamps) - 1
        while self.timestamps[-1] - self.timestamps[self.left] >= 300:
            self.left += 1

    def getHits(self, timestamp: int) -> int:
        if timestamp not in self.timestamp_map:
            self.hit(timestamp)
            self.timestamps.pop()
            del self.timestamp_map[timestamp]
        return len(self.timestamps[self.left:])


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
