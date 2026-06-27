class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = [0] * 26
        window[ord(s[0]) - ord('A')] = 1
        res = 1
        l = 0
        for r in range(1, len(s)):
            window[ord(s[r]) - ord('A')] += 1
            while max(window) < (r - l + 1) - k:
                window[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r - l +1)
        return res
                
            
            # X X Z Y X Y
            # l         r
            # k = 2
