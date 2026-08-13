class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        n = len(s) # len(s) == len(t) is guaranteed
        s_counts = [0] * 26
        t_counts = [0] * 26
        for i in range(n):
            s_counts[ord(s[i]) - ord('a')] += 1
            t_counts[ord(t[i]) - ord('a')] += 1
        
        return t_counts == s_counts