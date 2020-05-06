class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = 0
        max_num = max(nums)
        for i in range(len(nums)):
            temp += nums[i]
            if temp >= 0:
                max_num = max(max_num,temp)
            else:
                temp = 0
        return max_num
# Runtime: 60 ms, faster than 93.50% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 14.5 MB, less than 5.69% of Python3 online submissions for Maximum Subarray.