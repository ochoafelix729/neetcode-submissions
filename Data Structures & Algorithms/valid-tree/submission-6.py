from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) < n-1:
            return False
        
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        q = deque([[0,-1]]) # node, parent
        visited = set()

        while q:
            node, parent = q.popleft()
            visited.add(node)
            for nei in adj[node]:
                if nei in visited and nei != parent:
                    return False
                if nei == parent:
                    continue
                else:
                    q.append([nei,node])
                visited.add(nei)
        
        return len(visited) == n
