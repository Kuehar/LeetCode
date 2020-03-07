"""
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
"""

"""
Runtime:24ms
Memory:12.9MB
"""

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        Product = 1
        Sum = 0
        while n > 0:
            Product = Product * (n % 10)
            Sum = Sum + (n % 10)
            n //= 10
        return Product - Sum