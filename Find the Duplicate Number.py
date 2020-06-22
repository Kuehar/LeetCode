class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low,high = nums[0],nums[nums[0]]
        while low != high:
            low,high = nums[low],nums[nums[high]]
        low = 0
        while low != high:
            low,high = nums[low],nums[high]
        return low
# Runtime: 64 ms, faster than 86.19% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 16.4 MB, less than 35.59% of Python3 online submissions for Find the Duplicate Number.
