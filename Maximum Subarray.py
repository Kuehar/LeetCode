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


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        for i,num in enumerate(nums):            
            dp[i] = max(dp[i-1] + num, num)
        return max(dp)
# Runtime: 68 ms, faster than 58.99% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 15.1 MB, less than 19.90% of Python3 online submissions for Maximum Subarray.
