class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r = 0
        while True:
            for i in range(len(strs)):
                if r == len(strs[i]) or strs[i][r] != strs[0][r]:
                    return strs[0][:r] if r > 0 else ""
            r += 1
            


        