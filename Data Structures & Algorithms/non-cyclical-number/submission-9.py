class Solution:
    def isHappy(self, n: int) -> bool:

        def step(n: int) -> int:
            res = 0
            while n > 0:
                digit = n % 10
                res += (digit * digit)
                n //= 10
            return res

        slow = fast = n
        while True:
            slow = step(slow)
            fast = step(step(fast))

            if slow == 1 or fast == 1:
                return True

            if slow == fast:
                return False
