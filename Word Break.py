class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True]
        for i in range(1,len(s)+1):
            for j in wordDict:
                if i >= len(j) and s[i-len(j):i] == j and dp[i-len(j)] == True:
                    dp.append(True)
                    break
            if len(dp) <= i:
                dp.append(False)
        return dp[-1]
# Runtime: 28 ms, faster than 98.48% of Python3 online submissions for Word Break.
# Memory Usage: 14 MB, less than 36.33% of Python3 online submissions for Word Break.
