class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        for i in range(n):
            # odd length palindromes
            l, r = i, i
            while l in range(n) and r in range(n) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            # even length palindromes
            l, r = i, i + 1
            while l in range(n) and r in range(n) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        return res