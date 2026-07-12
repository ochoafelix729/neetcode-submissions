class Solution:
    def tribonacci(self, n: int) -> int:
        def trib(i):
            if i == 0:
                return 0
            if i <= 2:
                return 1
            
            if i in cache:
                return cache[i]
            cache[i] = trib(i-3) + trib(i-2) + trib(i-1)
            return cache[i]
        
        cache = {}
        return trib(n)