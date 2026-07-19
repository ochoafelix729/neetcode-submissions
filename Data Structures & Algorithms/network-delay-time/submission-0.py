class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1,n+1)} # node : list[(weight,node)]
        print(adj)
        for s, d, w in times:
            adj[s].append((w,d))
        
        min_times = {i: float('inf') for i in range(1,n+1)}
        min_times[k] = 0
        min_heap = [(0,k)]
        #res = float('inf')
        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            for w2, n2 in adj[n1]:
                if w2 > min_times[n2]:
                    continue
                
                if min_times[n1] + w2 < min_times[n2]:
                    heapq.heappush(min_heap, (w2, n2))
                    min_times[n2] = min_times[n1] + w2
                    #res = min(res, min_times[n2])

            
        print(min_times)

        return max(min_times.values()) if max(min_times.values()) < float('inf') else -1
        

