class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1,len(nums)+1):
            if nums[-i] == 0:
                nums.pop(-i)
                nums.append(0)
# Runtime: 52 ms, faster than 54.28% of Python3 online submissions for Move Zeroes.
# Memory Usage: 15 MB, less than 5.97% of Python3 online submissions for Move Zeroes.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        h = -1
        for i in range(len(nums)):
            if nums[i] != 0:
                h += 1
                nums[h], nums[i] = nums[i], nums[h]
# Runtime: 52 ms, faster than 54.28% of Python3 online submissions for Move Zeroes.
# Memory Usage: 15 MB, less than 5.97% of Python3 online submissions for Move Zeroes.