class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())

            elif token == '*':
                stack.append(stack.pop() * stack.pop())

            elif token == '/':
                denominator = stack.pop()
                numerator = stack.pop()
                stack.append(int(numerator/denominator))

            elif token == '-':
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)

            else:
                stack.append(int(token))
        return stack[-1]