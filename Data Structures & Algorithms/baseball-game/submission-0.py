class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0
        for op in operations:
            if op == '+':
                new_score = stack[-1] + stack[-2]
                stack.append(new_score)
                total += new_score
            elif op == 'D':
                new_score = stack[-1] * 2
                stack.append(new_score)
                total += new_score
            elif op == 'C':
                total -= stack.pop()
            else:
                stack.append(int(op))
                total += stack[-1]
        return total
