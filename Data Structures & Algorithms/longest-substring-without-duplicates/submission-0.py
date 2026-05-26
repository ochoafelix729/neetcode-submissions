from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window_set = set()
        
        max_length = 0
        curr_length = 0
        l, r = 0, 0
        while r < len(s):
            print(s[l], s[r], window_set)

            c = s[r]
            while c in window_set:
                window_set.remove(s[l])
                curr_length -= 1
                l += 1
            window_set.add(c)
            curr_length += 1
            max_length = max(max_length, curr_length)
            r += 1


        return max_length