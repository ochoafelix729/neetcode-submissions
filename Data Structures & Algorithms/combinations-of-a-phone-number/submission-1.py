class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_map = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }

        combs, comb = [], ""

        def backtrack(i, comb):
            # base case
            if len(comb) == len(digits):
                combs.append(comb)
                return

            options = digit_map[digits[i]]
            for ch in options:
                backtrack(i+1, comb + ch)
        
        backtrack(0, comb)
        return combs