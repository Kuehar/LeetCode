class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1]*len(nums)
        dp[-1] = 1
        for i in reversed(range(len(nums))):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)  
        return max(dp)
# Runtime: 1220 ms, faster than  44.36%  of  Python3  online submissions for  Longest Increasing Subsequence.
# Memory Usage: 14.1 MB, less than  28.52%  of  Python3  online submissions for  Longest Increasing Subsequence.
