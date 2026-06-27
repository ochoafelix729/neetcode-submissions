class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        res = 1
        window = {s[0]}
        l = 0
        for r in range(1, len(s)):
            if s[r] in window:
                while l < r and s[r] in window:
                    window.remove(s[l])
                    l += 1
            window.add(s[r])
            res = max(res, r-l+1)
        return res

        # x x x y
        # l     r