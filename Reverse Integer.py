class Solution:
    def reverse(self, x: int) -> int:
        # Constraints -2^31 <= x <= 2^31 - 1から
        # 32bit基準で考える
        max_32 = 2**31 - 1
        if abs(x) > max_32:
            return 0
        if x < 0:
            reverse_int = -int(str(abs(x))[::-1])
        else:
            reverse_int = int(str(x)[::-1])
        
        if abs(reverse_int) > max_32:
            return 0
        else:
            return reverse_int
# Runtime: 28 ms, faster than 86.13% of Python3 online submissions for Reverse Integer.
# Memory Usage: 14 MB, less than 9.77% of Python3 online submissions for Reverse Integer.
