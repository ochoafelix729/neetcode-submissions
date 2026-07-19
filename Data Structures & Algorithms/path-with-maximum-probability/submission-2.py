class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {i : [] for i in range(n)}
        for i in range(len(edges)):
            s, d = edges[i]
            p = succProb[i]
            adj[s].append((p, d))
            adj[d].append((p,s))
        
        max_probs = {i: 0 for i in range(n)}
        
        max_probs[start_node] = 1
        max_heap = [(1, start_node)]

        while max_heap:
            p1, n1 = heapq.heappop_max(max_heap)
            if p1 < max_probs[n1]:
                continue
            
            if n1 == end_node:
                return p1

            for p2, n2 in adj[n1]:
                new_prob = max_probs[n1] * p2
                
                if new_prob > max_probs[n2]:
                    heapq.heappush_max(max_heap, (new_prob, n2))
                    max_probs[n2] = new_prob
        
        return 0.0
