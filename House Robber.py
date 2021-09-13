class Solution:
    def rob(self, nums: List[int]) -> int:
        pre = cur = 0
        for i in nums:
            pre,cur = cur,max(pre+i,cur)
        return cur
# Runtime: 20 ms, faster than 98.32% of Python3 online submissions for House Robber.
# Memory Usage: 14.1 MB, less than 9.09% of Python3 online submissions for House Robber.

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1])
        
        dp = [-inf]*len(nums)
        dp[0],dp[1] = nums[0],max(nums[0],nums[1])
        
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
            
        return max(dp)
    
    
# Runtime: 28 ms, faster than 87.54% of Python3 online submissions for House Robber.
# Memory Usage: 14.2 MB, less than 51.36% of Python3 online submissions for House Robber.
