class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = 200
        for i in range(1, len(strs)):
            s1 = strs[i-1]
            s2 = strs[i]
            common = 0
            j = 0
            while j < min(len(s1), len(s2)) and s1[j] == s2[j]:
                common += 1
                j += 1
            longest = min(longest, common)
        return strs[0][:longest]