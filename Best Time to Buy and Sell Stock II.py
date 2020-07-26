class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pro = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                max_pro += prices[i+1] - prices[i] 
        return max_pro
# Runtime: 60 ms, faster than 88.25% of Python3 online submissions for Best Time to Buy and Sell Stock II.
# Memory Usage: 15.1 MB, less than 47.10% of Python3 online submissions for Best Time to Buy and Sell Stock II.
