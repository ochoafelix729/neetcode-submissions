class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:        
        # construct s1 table
        s1_table = {}
        for c in s1:
            if c not in s1_table:
                s1_table[c] = 1
            else:
                s1_table[c] += 1
        
        window = {}
        l = 0
        for r in range(len(s2)):
            if s2[r] not in window:
                window[s2[r]] = 1
            else:
                window[s2[r]] += 1
            if window == s1_table:
                return True
            if (r - l + 1) == len(s1):
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l += 1
        return False