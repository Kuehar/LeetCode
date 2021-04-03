# O(N) Solution

class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        for i in range(32):
            bits += (n&1)
            n = n >> 1
        return bits
# Runtime: 28 ms, faster than 89.38% of Python3 online submissions for Number of 1 Bits.
# Memory Usage: 14.1 MB, less than 90.33% of Python3 online submissions for Number of 1 Bits.


class Solution:
    def hammingWeight(self, n: int) -> int:
        sum = 0
        while n != 0:
            sum += 1
            n &= (n-1)
        return sum
# Runtime: 28 ms, faster than  89.33%  of  Python3  online submissions for  Number of 1 Bits.
# Memory Usage: 14.2 MB, less than  42.11%  of  Python3  online submissions for  Number of 1 Bits.

# https://www.kueharx.com/2021/04/pythonleetcode.html
