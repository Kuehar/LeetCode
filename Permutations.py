class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
# Runtime: 36 ms, faster than 87.99% of Python3 online submissions for Permutations.
# Memory Usage: 14.1 MB, less than 5.36% of Python3 online submissions for Permutations.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.dfs(nums, [], ans)
        return ans
    
    def dfs(self, nums, emp, ans):
        if not nums:
            ans.append(emp)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], emp+[nums[i]], ans)
# Runtime: 32 ms, faster than 96.70% of Python3 online submissions for Permutations.
# Memory Usage: 13.9 MB, less than 5.36% of Python3 online submissions for Permutations.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(first=0):
            if first == n:
                ans.append(nums[:])
            for i in range(first,n):
                nums[first],nums[i] = nums[i],nums[first]
                backtrack(first+1)
                nums[first],nums[i] = nums[i],nums[first]
        n = len(nums)
        ans = []
        backtrack()
        return ans
# Runtime: 40 ms, faster than 70.15% of Python3 online submissions for Permutations.
# Memory Usage: 14.2 MB, less than 89.82% of Python3 online submissions for Permutations.
