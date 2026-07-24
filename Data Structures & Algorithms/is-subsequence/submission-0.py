class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s and not t:
            return False
        if not s:
            return True
        
        i2 = 0
        for i1 in range(len(t)):
            if t[i1] == s[i2]:
                i2 += 1
                if i2 == len(s):
                    return True
        return False