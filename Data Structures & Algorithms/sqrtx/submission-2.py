class Solution:
    def mySqrt(self, x: int) -> int:

        low, high = 0, x
        while low <= high:
            mid = (low + high) // 2
            print(mid)
            if mid * mid == x or (mid * mid < x and (mid+1) * (mid+1) > x):
                return mid
            if mid * mid > x:
                high = mid-1
            else:
                low = mid+1

        # 33 = 5 * 5 + 8
        # 33 = 6 * 6 - 3