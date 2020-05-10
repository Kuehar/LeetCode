class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num,ans = set(sorted(nums)),[]
        for i in range(1,len(nums)+1):
            if i not in num:
                ans.append(i)
        return ans
# Runtime: 464 ms, faster than 11.82% of Python3 online submissions for Find All Numbers Disappeared in an Array.
# Memory Usage: 23.7 MB, less than 7.14% of Python3 online submissions for Find All Numbers Disappeared in an Array.

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            ans = abs(num) - 1
            if nums[ans] > 0:
                nums[ans] *= -1
        return [i+1 for i in range(len(nums)) if nums[i] > 0]
# Runtime: 380 ms, faster than 63.11% of Python3 online submissions for Find All Numbers Disappeared in an Array.
# Memory Usage: 21.5 MB, less than 17.86% of Python3 online submissions for Find All Numbers Disappeared 