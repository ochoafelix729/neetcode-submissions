class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(cap: int) -> int:
            ships, cur_cap = 1, cap
            for w in weights:
                if cur_cap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    cur_cap = cap
                cur_cap -= w
            return True

        low, high = max(weights), sum(weights)
        res = high
        while low <= high:
            cap = (low+high) // 2
            if canShip(cap):
                res = min(res, cap)
                high = cap-1
            else:
                low = cap+1
        
        return res
            