class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(x*x for x in nums)
# Runtime: 200 ms, faster than 98.52% of Python3 online submissions for Squares of a Sorted Array.
# Memory Usage: 16.3 MB, less than 31.98% of Python3 online submissions for Squares of a Sorted Array.
