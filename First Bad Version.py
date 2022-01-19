# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> int:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        for i in range(n):
            if isBadVersion(i):
                return i
        return n
# Time Limit Exceeded
# O(N)


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> int:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return n

        lo,hi = 0,n
        while lo < hi:
            mid = (lo+hi)//2
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid +1
        return lo
# Runtime: 52 ms, faster than 12.19% of Python3 online submissions for First Bad Version. O(logn)
# Memory Usage: 14.4 MB, less than 10.18% of Python3 online submissions for First Bad Version.
