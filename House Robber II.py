class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 2:
            return max(nums)
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))        
    
    def helper(self, nums):
        pre_max = cur_max = 0
        for num in nums:
            swap = cur_max
            cur_max = max(pre_max + num, cur_max)
            pre_max = swap
        return cur_max
# Runtime: 20 ms, faster than  99.72%  of  Python3  online submissions for  House Robber II.
# Memory Usage: 13.9 MB, less than  43.51%  of  Python3  online submissions for  House Robber II.



class Solution:
    def rob(self, nums: List[int]) -> int:        
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]
        # Exclude nums[0] or nums[-1],then you will only choose bigger number.
        # last two ans into max() are calcurated by using House Robber 1's function.
        numsExcludeLast = nums[:len(nums) - 1]
        numsExcludeFirst = nums[1:]
        excludeLastAns = self.robDP(numsExcludeLast)
        excludeFirstAns = self.robDP(numsExcludeFirst)
        return max(excludeLastAns, excludeFirstAns)
        
        
    # This code is used in House Robber 1
    def robDP(self, nums: List[int]):
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
    
    
# Runtime: 20 ms, faster than 99.40% of Python3 online submissions for House Robber II.
# Memory Usage: 14.5 MB, less than 6.14% of Python3 online submissions for House Robber II.


class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))
    
    def helper(self,nums):
        rob1 = rob2 = 0
        for n in nums:
            newRob = max(rob1+n,rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2
