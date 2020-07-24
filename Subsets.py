class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(temp,end):
            ans.append(temp+[])
            if len(nums) == len(temp):
                return
            for i in nums:
                if i > end:
                    temp.append(i)
                    dfs(temp,i)
                    temp.pop()
        dfs([],float(-inf))
        return ans
# Runtime: 32 ms, faster than 86.56% of Python3 online submissions for Subsets.
# Memory Usage: 13.8 MB, less than 90.09% of Python3 online submissions for Subsets.
