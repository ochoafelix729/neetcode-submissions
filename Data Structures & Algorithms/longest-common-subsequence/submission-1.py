class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n, m = len(text1), len(text2)
        cache = [[-1] * m for _ in range(n)]

        def dfs(i, j):
            if i == n or j == m:
                return 0

            if cache[i][j] != -1:
                return cache[i][j]
            
            if text1[i] == text2[j]:
                cache[i][j] = 1 + dfs(i+1, j+1)
                return cache[i][j]
            
            if text1[i] != text2[j]:
                cache[i][j] = max(dfs(i, j+1), dfs(i+1, j))
                return cache[i][j]
        
        return dfs(0,0)
