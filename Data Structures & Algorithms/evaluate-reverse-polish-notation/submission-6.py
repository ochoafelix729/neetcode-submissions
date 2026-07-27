class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        print(-36 // 13)
        for tok in tokens:
            if tok == '+':
                stack.append(stack.pop() + stack.pop())
            elif tok == '-':
                first = stack.pop()
                second = stack.pop()
                stack.append(second-first)
            elif tok == '*':
                stack.append(stack.pop() * stack.pop())
            elif tok == '/':
                first = stack.pop()
                second = stack.pop()
                if first < 0 or second < 0:
                    res = -1 * (abs(second) // abs(first))
                else:
                    res = second // first
                stack.append(res)
            else:
                stack.append(int(tok))
            print(stack)
        return stack[-1]