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
# Runtime: 240 ms, faster than 5.15% of Python3 online submissions for Power of Three.
# Memory Usage: 14.4 MB, less than 13.91% of Python3 online submissions for Power of Three.


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1
#Runtime: 68 ms, faster than 87.60% of Python3 online submissions for Power of Three.
#Memory Usage: 14.3 MB, less than 46.96% of Python3 online submissions for Power of Three.
