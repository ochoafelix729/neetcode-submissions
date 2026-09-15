class DSU:
    def __init__(self, n):
        self.rank = {i: 0 for i in range(n)}
        self.par = {i: i for i in range(n)}

    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True
        
    def find(self, n):
        while n != self.par[n]:
            self.par[n] = self.par[self.par[n]]
            n = self.par[n]
        return n

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        components = n
        for a, b in edges:
            if dsu.union(a,b):
                components -= 1
        return components




        