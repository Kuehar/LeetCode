class Solution:
    def calc(self,nums,index,sums,S):
        if index == len(nums):
            if sums == S:
                self.count += 1
        else:
            self.calc(nums,index+1,sums+nums[index],S)
            self.calc(nums,index+1,sums-nums[index],S)

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.count = 0
        self.calc(nums,0,0,S)
        return self.count
# Time Limit Exceeded


from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:

        @lru_cache(None)
        def calc(index,S):
            if index == 0:
                 return  int(nums[0] == S) + int(-nums[0] == S)
            return  calc(index-1, S - nums[index]) + calc(index-1, S + nums[index])

        return calc(len(nums)-1, S)
# Runtime: 240 ms, faster than 74.28% of Python3 online submissions for Target Sum.
# Memory Usage: 31.5 MB, less than 50.00% of Python3 online submissions for Target Sum.
