class Solution:
    def firstUniqChar(self, s: str) -> int:
        occurences = [0] * 26
        indices = [-1] * 26

        for i, ch in enumerate(s):
            occurences[ord(ch) - ord('a')] += 1
            indices[ord(ch) - ord('a')] = i
        
        res = float('inf')
        for i in range(len(occurences)):
            if occurences[i] == 1 and indices[i] < res:
                res = indices[i]

        return res if res != float('inf') else -1
