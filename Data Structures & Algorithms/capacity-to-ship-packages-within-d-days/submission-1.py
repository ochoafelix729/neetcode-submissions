class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap: int) -> bool:
            cur_cap = cap
            cur_days = 1
            for w in weights:
                if cur_cap - w < 0:
                    cur_cap = cap
                    cur_days += 1
                    if cur_days > days:
                        return False
                cur_cap -= w
            return True
        
        while l <= r:
            cap = (l+r) // 2
            if canShip(cap):
                res = min(res, cap)
                r = cap-1
            else:
                l = cap+1
        
        return res