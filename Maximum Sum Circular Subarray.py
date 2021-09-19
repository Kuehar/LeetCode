class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # range[1,len(nums)],とrange[len(nums)-1],nums[0]+nums[-1]で解けばまあいけそう。
        # 計算量はやばそうだけど・・・
        dp1 = dp2 = [0]*len(nums)
        dp1[0] = max(dp1[0],nums[1])
        for i in range(1,len(nums)):
            dp1[i] = max(dp1[i-1] + nums[i], nums[i])
        max_num1 = max(dp1)
        
        dp2[0] = max(dp2[0],nums[1])
        for j in range(1,len(nums)-1):
            dp2[i] = max(dp2[i-1],dp2[i-1]+nums[i])
            
        max_num2 = max(dp2)
        
        return max(max_num1,max_num2,(nums[0]+nums[-1]))
