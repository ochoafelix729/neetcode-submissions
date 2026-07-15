class Solution:
    def integerBreak(self, n: int) -> int:
        cache = [0] * (n+1)
        def dfs(num):
            if num == 1:
                return 1
            
            if cache[num]:
                return cache[num]

            res = 0 if num == n else num
            
            for i in range(1, num):
                val = dfs(num-i) * dfs(i)
                res = max(res, val)
                cache[num] = res

            return cache[num]
        
        return dfs(n)





