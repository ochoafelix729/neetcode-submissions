class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        def canEatBananas(k: int) -> bool:
            hours_taken = 0
            for p in piles:
                if p % k == 0:
                    hours_taken += (p // k)
                else:
                    hours_taken += (p // k) + 1
                if hours_taken > h:
                    return False
            return True
        
        while l <= r:
            k = (l+r) // 2
            print(k)
            if canEatBananas(k):
                res = min(res, k)
                r = k-1
            else:
                l = k+1
        return res