class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        for i in range(2,n+1):
            for j in range(1,int(i ** 0.5)+1):
                dp[i] = min(dp[i],dp[i-j*j]+1)
        return dp[n]
# Runtime: 4608 ms, faster than 39.65% of Python3 online submissions for Perfect Squares.
# Memory Usage: 14 MB, less than 60.54% of Python3 online submissions for Perfect Squares.
