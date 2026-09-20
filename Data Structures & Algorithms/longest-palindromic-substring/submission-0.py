class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        resL, resR = 0, 0
        n = len(s)
        for i in range(n):
            # odd length palindromes
            l, r = i, i
            while l in range(n) and r in range(n) and s[l] == s[r]:
                if r - l + 1 > longest:
                    resL, resR = l, r
                    longest = r - l + 1
                l -= 1
                r += 1

            # even length palindromes
            l, r = i, i + 1
            while l in range(n) and r in range(n) and s[l] == s[r]:
                if r - l + 1 > longest:
                    resL, resR = l, r
                    longest = r - l + 1
                l -= 1
                r += 1
        
        return s[resL: resR + 1]