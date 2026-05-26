class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0

        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            print(prices[l], prices[r])
            profit = prices[r] - prices[l]
            if profit < 0:
                l += 1
            elif profit > max_profit:
                max_profit = profit
            r += 1

            while l < r and r == (len(prices)-1):
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
                l += 1
                
        return max_profit