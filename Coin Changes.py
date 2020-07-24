class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount + 1] * amount
        dp[0] = 0
        for i in range(amount+1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i],dp[i-c]+1)
        return -1 if dp[amount] > amount else dp[amount]
# Runtime: 1604 ms, faster than 51.63% of Python3 online submissions for Coin Change.
# Memory Usage: 14 MB, less than 65.21% of Python3 online submissions for Coin Change.
