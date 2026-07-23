class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        # prims solution

        def distance(n1, n2):
            return abs(n1[0] - n2[0]) + abs(n1[1] - n2[1])

        n = len(points)
        adj = {i : [] for i in range(n)}
        for i in range(n):
            for j in range(i+1, n):
                dist = distance(points[j], points[i])
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        #print(adj)
        
        minheap = [(0,0)] # dist, index
        visited = set()
        cost = 0
        connected_points = -1
        while minheap:
            dist, index = heapq.heappop(minheap)

            if index in visited:
                continue

            cost += dist
            connected_points += 1
            visited.add(index)

            if connected_points == n-1:
                return cost

            for nei in adj[index]:
                if nei[1] not in visited:
                    heapq.heappush(minheap, nei)


        # kruskals solution

        # def distance(n1, n2):
        #     return abs(n1[0] - n2[0]) + abs(n1[1] - n2[1])

        # def find(node):
        #     cur = node
        #     while cur != par[cur]:
        #         par[cur] = par[par[cur]]
        #         cur = par[cur]
        #     return cur
        
        # def union(n1, n2):
        #     p1, p2 = find(tuple(n1)), find(tuple(n2))
        #     if p1 == p2:
        #         return False
            
        #     if rank[p1] > rank[p2]:
        #         par[p2] = p1
        #     elif rank[p2] > rank[p1]:
        #         par[p1] = p2
        #     else:
        #         par[p1] = p2
        #         rank[p2] += 1
        #     return True
        
        # if len(points) == 1:
        #     return 0

        # # build edges
        # edges = [] # dist, point1, point2
        # for i in range(len(points)):
        #     for j in range(1, len(points)):
        #         point1 = points[i]
        #         point2 = points[j]
        #         dist = distance(point1, point2)
        #         edges.append((dist, point1, point2))
        
        # # set up DSU
        # par = {}
        # rank = {}
        # for i in range(len(points)):
        #     par[tuple(points[i])] = tuple(points[i])
        #     rank[tuple(points[i])] = 0

        # # run kruskals
        # edges.sort()
        # cost = 0
        # connected_points = 0
        # for dist, point1, point2 in edges:
        #     if not union(point1, point2):
        #         continue
            
        #     cost += dist
        #     connected_points += 1
        #     if connected_points == len(points) - 1:
        #         return cost
        