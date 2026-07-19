class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        print(edges)
        edges.sort()
        
        visited = set()
        visited.add(0)
        for p, c in edges:
            if p not in visited and c not in visited:
                return False

            if p in visited:
                if c in visited:
                    return False
                visited.add(c)
            
            elif c in visited:
                if p in visited:
                    return False
                visited.add(p)
        
        return True