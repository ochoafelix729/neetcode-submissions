class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for x in range(1, amount+1):
            candidates = []
            for c in coins:
                if x-c >= 0:
                    candidates.append(dp[x-c])
            if len(candidates) > 0:
                dp[x] = 1 + min(candidates)
        
        print(dp)
        return dp[-1] if dp[-1] != float('inf') else -1
    
    # 1 5 10
    # 