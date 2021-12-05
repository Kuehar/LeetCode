class Solution:
    def rob(self, nums: List[int]) -> int:
        pre = cur = 0
        for i in nums:
            pre,cur = cur,max(pre+i,cur)
        return cur
# Runtime: 20 ms, faster than 98.32% of Python3 online submissions for House Robber.
# Memory Usage: 14.1 MB, less than 9.09% of Python3 online submissions for House Robber.

cclass Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l < 0:
            return 0
        elif l == 1:
            return nums[0]
        elif l == 2:
            return max(nums[0],nums[1])
        
        dp = [-inf]*l
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        
        for i in range(2,l):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
            
        return max(dp)
# Runtime: 20 ms, faster than 99.30% of Python3 online submissions for House Robber.
# Memory Usage: 14.2 MB, less than 52.69% of Python3 online submissions for House Robber.

# Recursive and memo
class Solution:
    def __init__(self):
        self.memo = {}
    
    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        return self.robFrom(0,nums)
    
    
    def robFrom(self,i,nums):
        # no more houses left to examine.
        if i >= len(nums):
            return 0
        if i in self.memo:
            return self.memo[i]
            
        ans = max(self.robFrom(i+1,nums),self.robFrom(i+2,nums)+nums[i])
            
        self.memo[i] = ans
        return ans
# Runtime: 32 ms, faster than 66.56% of Python3 online submissions for House Robber.
# Memory Usage: 14.1 MB, less than 78.62% of Python3 online submissions for House Robber.
