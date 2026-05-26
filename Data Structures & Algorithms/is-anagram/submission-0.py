from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_table = defaultdict(int)
        t_table = defaultdict(int)

        for c in s:
            s_table[c] += 1
        
        for c in t:
            t_table[c] += 1

        return s_table == t_table
            