class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p, s] for p, s in zip(position, speed)]

        stack = []
        print(cars)
        for p, s in sorted(cars)[::-1]:
            stack.append((target - p) / s) # time to reach target
            
            if len(stack) >= 2:
                if stack[-1] <= stack[-2]:
                    stack.pop()
            print(stack)
        return len(stack)