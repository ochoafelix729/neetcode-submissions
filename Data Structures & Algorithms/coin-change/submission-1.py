class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(cur_sum):
            if cur_sum == amount:
                return 0

            if cur_sum > amount:
                return float('inf')
            
            if cur_sum in cache:
                return cache[cur_sum]

            ans = float('inf')

            for coin in coins:
                ans = min(ans, 1 + dfs(cur_sum + coin))

            cache[cur_sum] = ans
            return cache[cur_sum]

        res = dfs(0)
        return -1 if res == float('inf') else res