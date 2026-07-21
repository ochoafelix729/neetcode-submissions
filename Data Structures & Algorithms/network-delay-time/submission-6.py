class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # djikstra's algorithm
        adj = {i: [] for i in range(1,n+1)}
        for u,v,t in times:
            adj[u].append((t,v))

        best_times = {i: float('inf') for i in range(1,n+1)}
        best_times[k] = 0
        
        minheap = [(0,k)]
        res = -1
        while minheap:
            t1,n1 = heapq.heappop(minheap)
            if t1 > best_times[n1]:
                continue
            
            for t2, n2 in adj[n1]:
                if best_times[n1] + t2 < best_times[n2]:
                    heapq.heappush(minheap, (t2,n2))
                    best_times[n2] = best_times[n1] + t2
        
        maxx = max(best_times.values())
        return res if maxx == float('inf') else maxx
        

