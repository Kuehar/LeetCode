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
