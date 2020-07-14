class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums.count(target) == 0:
            return -1
        else:
            ans = nums.index(target)
        return ans
# Runtime: 36 ms, faster than 92.59% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 14 MB, less than 61.16% of Python3 online submissions for Search in Rotated Sorted Array.
