class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                max_count = max(max_count,count)
                count = 0
        return max(max_count,count)
# Runtime: 332 ms, faster than 98.29% of Python3 online submissions for Max Consecutive Ones.
# Memory Usage: 14.5 MB, less than 16.28% of Python3 online submissions for Max Consecutive Ones.
