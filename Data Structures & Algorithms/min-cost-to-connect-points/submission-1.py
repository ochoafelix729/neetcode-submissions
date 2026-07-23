class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        # kruskals solution

        def distance(n1, n2):
            return abs(n1[0] - n2[0]) + abs(n1[1] - n2[1])

        def find(node):
            cur = node
            while cur != par[cur]:
                par[cur] = par[par[cur]]
                cur = par[cur]
            return cur
        
        def union(n1, n2):
            p1, p2 = find(tuple(n1)), find(tuple(n2))
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p2] > rank[p1]:
                par[p1] = p2
            else:
                par[p1] = p2
                rank[p2] += 1
            return True
        
        if len(points) == 1:
            return 0

        # build edges
        edges = [] # dist, point1, point2
        for i in range(len(points)):
            for j in range(1, len(points)):
                point1 = points[i]
                point2 = points[j]
                dist = distance(point1, point2)
                edges.append((dist, point1, point2))
        
        # set up DSU
        par = {}
        rank = {}
        for i in range(len(points)):
            par[tuple(points[i])] = tuple(points[i])
            rank[tuple(points[i])] = 0

        # run kruskals
        edges.sort()
        cost = 0
        connected_points = 0
        for dist, point1, point2 in edges:
            if not union(point1, point2):
                continue
            
            cost += dist
            connected_points += 1
            if connected_points == len(points) - 1:
                return cost
        




