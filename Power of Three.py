class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        for i in range(31):
            if pow(3,i) == n:
                return True
        return False
# Runtime: 248 ms, faster than 5.15% of Python3 online submissions for Power of Three.
# Memory Usage: 14.2 MB, less than 75.52% of Python3 online submissions for Power of Three.
# This solution is simple,but stupid one.

