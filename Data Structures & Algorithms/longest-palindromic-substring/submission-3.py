class Solution:
    def longestPalindrome(self, s: str) -> str:
        resL, resR = 0, 0
        resLen = 1
        n = len(s)
        for i in range(n):
            # odd length palindromes
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > resLen:
                    resLen = r - l + 1
                    resL, resR = l, r
                l -= 1
                r += 1

            # even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > resLen:
                    resLen = r - l + 1
                    resL, resR = l, r
                l -= 1
                r += 1
        
        return s[resL: resR + 1]