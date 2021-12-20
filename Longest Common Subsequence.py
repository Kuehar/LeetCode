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
