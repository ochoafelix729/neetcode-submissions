class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        
        # construct s1 table
        s1_counts = {}
        for c in s1:
            s1_counts[c] = 1 + s1_counts.get(c, 0)
        print(s1_counts)

        # init sliding table
        window_counts = {}

        # construct first window
        l, r = 0, 0
        while r < len(s1):
            window_counts[s2[r]] = 1 + window_counts.get(s2[r], 0)
            r += 1
        if s1_counts == window_counts: return True
        
        window_counts[s2[l]] -= 1
        if window_counts[s2[l]] == 0: window_counts.pop(s2[l])
        l += 1

        

        # slide window
        while r < len(s2):
            # print("window:", s2[l], s2[r])
            window_counts[s2[r]] = 1 + window_counts.get(s2[r], 0)
            print(window_counts)
            if s1_counts == window_counts: return True
            
            window_counts[s2[l]] -= 1
            if window_counts[s2[l]] == 0: window_counts.pop(s2[l])
            l += 1
            r += 1

        return False