class Solution:
    def rob(self, nums: List[int]) -> int:
        pre = cur = 0
        for i in nums:
            pre,cur = cur,max(pre+i,cur)
        return cur
# Runtime: 20 ms, faster than 98.32% of Python3 online submissions for House Robber.
# Memory Usage: 14.1 MB, less than 9.09% of Python3 online submissions for House Robber.
