class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low,high = nums[0],nums[nums[0]]
        while low != high:
            low,high = nums[low],nums[nums[high]]
        low = 0
        while low != high:
            low,high = nums[low],nums[high]
        return low
# Runtime: 64 ms, faster than 86.19% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 16.4 MB, less than 35.59% of Python3 online submissions for Find the Duplicate Number.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return       
        ans,index = 0,1
        nums = sorted(nums)
        for i in range(1,len(nums)):
            if nums[i] == nums[index-1]:
                ans = nums[i]
                index += 1
            else:
                index += 1
        return ans
# Runtime: 68 ms, faster than 55.74% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 16.6 MB, less than 78.10% of Python3 online submissions for Find the Duplicate Number.
