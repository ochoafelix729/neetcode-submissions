class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol, cur_string = [], ""

        def isValid(string):
            stack = ['dummy']
            for ch in string:
                if len(stack) == 0:
                    return False
                if ch == '(':
                    stack.append('(')
                else:
                    stack.pop()
            return len(stack) == 1
                

        def backtrack(cur_string):
            # base cases
            if len(cur_string) == n*2:
                if isValid(cur_string):
                    sol.append(cur_string)
                return
            
            # add left parentheses
            backtrack(cur_string + '(')

            # add right parentheses
            backtrack(cur_string + ')')
        
        backtrack(cur_string)
        return sol