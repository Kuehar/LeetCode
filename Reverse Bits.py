class Solution:
    def reverseBits(self, n: int) -> int:
        ret,power = 0,31
        while n:
            ret += (n&1) << power
            n = n >> 1
            power -= 1
        return ret
# Runtime: 32 ms, faster than 63.77% of Python3 online submissions for Reverse Bits.
# Memory Usage: 14.2 MB, less than 19.86% of Python3 online submissions for Reverse Bits.
