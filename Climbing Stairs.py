class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        num1, num2 = 0, 1
        for i in range(n):
            num1, num2 = num2, num1+num2
        return num2
# Runtime: 32 ms, faster than 39.40% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 13.7 MB, less than 5.97% of Python3 online submissions for Climbing Stairs.


from functools import lru_cache

class Solution:
    @lru_cache(None)
    def climbStairs(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
# Runtime: 24 ms, faster than 91.08% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 13.9 MB, less than 5.97% of Python3 online submissions for Climbing Stairs.
