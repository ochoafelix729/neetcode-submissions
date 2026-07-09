from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        delta = defaultdict(int)
        for src, dest in trust:
            delta[src] -= 1
            delta[dest] += 1

        for person, delta in delta.items():
            if delta == n-1:
                return person
        return -1