class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        ans,mod = 0,10**9+7
        nums.sort()
        for i,j in enumerate(nums):
            if target < j*2:
                break
            b = bisect.bisect(nums,target-j,lo=i)
            ans += pow(2, b-i-1, mod)
        return ans % mod
# Runtime: 888 ms, faster than 82.84% of Python3 online submissions for Number of Subsequences That Satisfy the Given Sum Condition.
# Memory Usage: 25.2 MB, less than 100.00% of Python3 online submissions for Number of Subsequences That Satisfy the Given Sum Condition.
