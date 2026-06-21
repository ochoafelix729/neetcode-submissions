class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                prev_idx, prev_temp = stack.pop()
                res[prev_idx] = i - prev_idx
            stack.append((i, temp))
        
        return res

        # 45 44 43 42 50
        # 50