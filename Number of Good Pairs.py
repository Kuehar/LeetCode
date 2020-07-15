class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans,dic = 0,{}
        for i,j in enumerate(nums):
            if j in dic:
                ans += dic[j]
                dic[j] += 1
            else:
                dic[j] = 1
        return ans
# Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Number of Good Pairs.
# Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Number of Good Pairs.
