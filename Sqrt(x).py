# Using library

import math

class Solution:
    def mySqrt(self, x: int) -> int:
        return int(abs(math.sqrt(x)))
        
# Runtime: 32 ms, faster than 78.95% of Python3 online submissions for Sqrt(x).
# Memory Usage: 14.1 MB, less than 78.73% of Python3 online submissions for Sqrt(x).

# scratch Program with binary search

class Solution:
    def mySqrt(self, x: int) -> int:
        low,high = 0,x
        while low <= high:
            mid = low + (high - low) //2
            if mid*mid <= x < (mid+1) * (mid+1):
                return mid
            elif x < mid*mid:
                high = mid-1
            else:
                low = mid+1
                
# Runtime: 40 ms, faster than 38.20% of Python3 online submissions for Sqrt(x).
# Memory Usage: 14.3 MB, less than 13.70% of Python3 online submissions for Sqrt(x).
