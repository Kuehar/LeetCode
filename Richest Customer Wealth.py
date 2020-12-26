class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = []
        for i in range(len(accounts)):
            ans.append(sum(accounts[i]))
        return max(ans)
# Runtime: 48 ms, faster than 93.45% of Python3 online submissions for Richest Customer Wealth.
# Memory Usage: 14.3 MB, less than 28.87% of Python3 online submissions for Richest Customer Wealth.
