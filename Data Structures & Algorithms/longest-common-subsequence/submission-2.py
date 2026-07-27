from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n, m = len(text1), len(text2)

        @cache
        def dfs(i, j):
            if i == n or j == m:
                return 0
            
            if text1[i] == text2[j]:
                return 1 + dfs(i+1, j+1)
            
            if text1[i] != text2[j]:
                return max(dfs(i, j+1), dfs(i+1, j))
        
        return dfs(0,0)
