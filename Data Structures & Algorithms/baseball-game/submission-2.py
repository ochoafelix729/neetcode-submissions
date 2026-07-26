class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for op in operations:
            if op == '+':
                inter = (stack[-1] + stack[-2])
                res += inter
                stack.append(inter)
            elif op == 'D':
                inter = (stack[-1] * 2)
                res += inter
                stack.append(inter)
            elif op == 'C':
                res -= stack.pop()
            else:
                stack.append(int(op))
                res += stack[-1]
        return res