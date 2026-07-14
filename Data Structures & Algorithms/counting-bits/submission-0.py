class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            i_copy = i
            count = 0
            while i_copy > 0:
                if i_copy & 1 == 1:
                    count += 1
                i_copy = i_copy >> 1
            res.append(count)
        return res