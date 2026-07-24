class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1

        first, second, third = 0, 1, 1
        for _ in range(3, n+1):
            nxt = first + second + third
            first = second
            second = third
            third = nxt
        return third


        # cache = [-1] * (n+1)

        # def dfs(i):
        #     if i == 0:
        #         return 0
        #     if i <= 2:
        #         return 1

        #     if cache[i] != -1:
        #         return cache[i]
            
        #     cache[i] = dfs(i-1) + dfs(i-2) + dfs(i-3)
        #     return cache[i]

        # return dfs(n)
            
