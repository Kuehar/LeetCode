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


