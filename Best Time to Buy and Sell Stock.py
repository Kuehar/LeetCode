class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx, mn = 0, prices and prices[0]
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                mx = max(mx,prices[i]-mn)
            else:
                mn = min(mn,prices[i])
        return mx
# Runtime: 68 ms, faster than 43.79% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 15.2 MB, less than 5.75% of Python3 online submissions for Best Time to Buy and Sell Stock.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx, mn = 0, float('inf')
        for price in prices:
            mn = min(mn, price)
            pro = price - mn
            mx = max(mx, pro)
        return mx
# Runtime: 72 ms, faster than 26.68% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 15.1 MB, less than 5.75% of Python3 online submissions for Best Time to Buy and Sell Stock.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = min_price = 0
        min_price = prices[0]
        for i in range(1,len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            if max_profit < prices[i] - min_price:
                max_profit = prices[i] - min_price
        return max_profit
    
# Runtime: 968 ms, faster than 76.13% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25 MB, less than 81.10% of Python3 online submissions for Best Time to Buy and Sell Stock.
