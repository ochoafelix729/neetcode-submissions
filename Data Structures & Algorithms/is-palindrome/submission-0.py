class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_s = ""
        for c in s:
            if c.isalnum():
                alnum_s += c.lower()

        print(alnum_s)

        l, r = 0, len(alnum_s)-1
        
        while r > l:
            if alnum_s[r] != alnum_s[l]:
                return False
            r -= 1
            l += 1
        
        return True