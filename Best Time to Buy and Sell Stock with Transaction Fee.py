class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash,hold = 0,-prices[0]
        print(hold)
        for i in range(1,len(prices)):
            cash = max(cash,hold+prices[i]-fee)
            hold = max(hold,cash-prices[i])
        return cash
# Runtime: 720 ms, faster than 36.46% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
# Memory Usage: 21.4 MB, less than 53.85% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
