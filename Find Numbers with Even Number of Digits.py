"""
Runtime:56ms
Memory:13MB
slower than other 55% solutions
"""

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        digits = 0
        for i,name in enumerate(nums):
            if len(str(nums[i]))%2 == 0:
                digits = digits + 1
            else:
                pass
        return digits
