class Solution:
    def longestCommonSubsequence(self, X: str, Y: str) -> int:
        dp = [[0 for i in range(len(X)+1)] for j in range(len(Y)+1)]
        for i in range(len(Y)):
            for j in range(len(X)):
                if X[j] ==  Y[i]:
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
        return max(list(map(lambda x: max(x), dp)))
# Runtime: 412 ms, faster than 67.07% of Python3 online submissions for Longest Common Subsequence.
# Memory Usage: 22.8 MB, less than 54.94% of Python3 online submissions for Longest Common Subsequence.
# Time Complexity O(N^2)

from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @lru_cache(maxsize=None)
        def memo_solve(p1,p2):
            if p1 == len(text1) or p2 == len(text2):
                    return 0
            option_1 = memo_solve(p1+1,p2)
            first_occurence = text2.find(text1[p1],p2)
            option_2 = 0
            
            if first_occurence != -1:
                option_2 = 1+memo_solve(p1+1,first_occurence+1)
                
            return max(option_1,option_2)
        
        return memo_solve(0,0)
# Runtime: 1000 ms, faster than 16.52% of Python3 online submissions for Longest Common Subsequence.
# Memory Usage: 145 MB, less than 5.36% of Python3 online submissions for Longest Common Subsequence.
# Time Complexity O(M⋅N^2).
# Space Complexity O(M⋅N).
