# ビット操作の例
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            ans ^= n
        return ans
# Runtime: 80 ms, faster than 93.89% of Python3 online submissions for Single Number.
# Memory Usage: 16.5 MB, less than 6.56% of Python3 online submissions for Single Number.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        while len(nums) > 0:
            num = nums.pop(0)
            if num in nums:
                nums.pop(0)
            else:
                return num

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)
