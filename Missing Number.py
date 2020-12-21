# BruteForce
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i not in nums:
                return i
        return max(nums)+1
# Runtime: 2392 ms, faster than 10.65% of Python3 online submissions for Missing Number.
# Memory Usage: 15.2 MB, less than 60.09% of Python3 online submissions for Missing Number.

# Using HashSet
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(nums)
        for i in range(len(nums)+1):
            if i not in s:
                return i
# Runtime: 124 ms, faster than 84.82% of Python3 online submissions for Missing Number.
# Memory Usage: 16 MB, less than 5.92% of Python3 online submissions for Missing Number.
