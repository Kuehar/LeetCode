class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums
# Runtime: 181 ms, faster than 5.02% of Python3 online submissions for Concatenation of Array.
# Memory Usage: 14 MB, less than 98.94% of Python3 online submissions for Concatenation of Array.
