class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        num = sorted(nums)
        for i in range(len(nums)):
            ans.append(num.index(nums[i]))
        return ans
# Runtime: 92 ms, faster than 55.84% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
# Memory Usage: 13.8 MB, less than 79.58% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        return [sorted_nums.index(num) for num in nums]
# Runtime: 100 ms, faster than 54.35% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
# Memory Usage: 13.9 MB, less than 41.13% of Python3 online submissions for How Many Numbers Are 
