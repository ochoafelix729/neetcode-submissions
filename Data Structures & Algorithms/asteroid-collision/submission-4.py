class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                b = stack[-1]
                if abs(a) == abs(b):
                    stack.pop()
                    a = 0
                elif abs(a) < abs(b):
                    a = 0
                else:
                    stack.pop()
            if a:
                stack.append(a)
        
        return stack
        