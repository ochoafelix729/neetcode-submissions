class Leaderboard:

    def __init__(self):
        self.leaderboard = [] # heap
        self.activeScore = defaultdict(int)
        self.version = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.activeScore[playerId] += score
        self.version[playerId] += 1
        heapq.heappush(
            self.leaderboard,
            (-self.activeScore[playerId], playerId, self.version[playerId])
        )

    def top(self, K: int) -> int:
        res = 0
        toAdd = []
        while self.leaderboard and K > 0:
            score, playerId, version = heapq.heappop(self.leaderboard)
            if version != self.version[playerId]:
                continue

            res -= score
            K -= 1
            toAdd.append((score, playerId, version))

        for el in toAdd:
            heapq.heappush(self.leaderboard, el)

        return res

    def reset(self, playerId: int) -> None:
        self.activeScore[playerId] = 0
        self.version[playerId] += 1


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
