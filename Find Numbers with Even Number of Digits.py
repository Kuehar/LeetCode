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

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            count = 0
            while n >= 1:
                n /= 10
                count += 1
            if count % 2 == 0:
                ans += 1
            count = 0
        return ans
# Runtime: 93 ms, faster than 16.36% of Python3 online submissions for Find Numbers with Even Number of Digits.
# Memory Usage: 13.9 MB, less than 99.83% of Python3 online submissions for Find Numbers with Even Number of Digits.
