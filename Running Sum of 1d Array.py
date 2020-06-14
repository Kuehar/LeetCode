class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return itertools.accumulate(nums)
# Runtime: 60 ms, faster than 33.33% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 14.1 MB, less than 33.33% of Python3 online submissions for Running Sum of 1d Array.


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        i = 1
        while i<len(nums):
            nums[i] += nums[i-1]
            i += 1
        return nums
# Runtime: 44 ms, faster than 33.33% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Running Sum of 1d Array.
