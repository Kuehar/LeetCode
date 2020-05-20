class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start = last = 0
        num = sorted(nums)
        for i in range(len(nums)):
            if nums[i] != num[i]:
                start = i
                break
        for i in range(len(nums)-1,-1,-1):
            if nums[i] != num[i]:
                last = i
                break
        return last - start + 1 if last - start else 0
# Runtime: 196 ms, faster than 98.85% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
# Memory Usage: 15.2 MB, less than 5.00% of Python3 online submissions for Shortest Unsorted Continuous Subarray
