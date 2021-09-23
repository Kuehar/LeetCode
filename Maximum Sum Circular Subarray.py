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

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # ただ比較する。
        ans1 = cur = -inf
        for x in nums:
            cur = x+max(cur, 0)
            ans1 = max(ans1, cur)

        # 最も少ない値を割り出し、numsの合計値から引く。範囲はnums[1:len(nums)]
        ans2 = cur = float('inf')
        for i in range(1, len(nums)):
            cur = nums[i] + min(cur, 0)
            ans2 = min(ans2, cur)
        ans2 = sum(nums) - ans2

        # 最も少ない値を割り出し、numsの合計値から引く。範囲はnums[len(nums)-1]
        ans3 = cur = float('inf')
        for i in range(len(nums)-1):
            cur = nums[i] + min(cur, 0)
            ans3 = min(ans3, cur)
        ans3 = sum(nums) - ans3
        
        return max(ans1, ans2, ans3)
