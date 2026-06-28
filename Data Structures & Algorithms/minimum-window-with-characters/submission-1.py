from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = defaultdict(int)
        for c in t:
            t_counts[c] += 1
        print(t_counts)
        
        equals = defaultdict(int)
        extras = defaultdict(int)
        res = s + "extra fluff"
        l = 0
        for r in range(len(s)):
            if s[r] in t_counts:
                if equals[s[r]] < t_counts[s[r]]:
                    equals[s[r]] += 1
                else:
                    extras[s[r]] += 1
            while equals == t_counts:
                if len(s[l:r+1]) < len(res):
                    res = s[l:r+1]
                if s[l] in t_counts:
                    if extras[s[l]] > 0:
                        extras[s[l]] -= 1
                    else:
                        equals[s[l]] -= 1
                l += 1
        
        return "" if res == s + "extra fluff" else res



