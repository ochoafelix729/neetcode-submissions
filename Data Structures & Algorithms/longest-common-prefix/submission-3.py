class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        i = 0
        while True:
            if i >= len(strs[0]):
                return lcp
            ch = strs[0][i]
            for wrd in strs[1:]:
                if i >= len(wrd) or wrd[i] != ch:
                    return lcp
            lcp += ch
            i += 1

        return lcp