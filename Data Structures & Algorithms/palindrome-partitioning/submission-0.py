class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, partition = [], []

        def isPalindrome(word, l, r):
            while l <= r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(i):
            # base case
            if i == len(s):
                res.append(partition.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    partition.append(s[i:j+1])
                    print(partition)
                    backtrack(j+1)
                    partition.pop()

        backtrack(0)
        return res