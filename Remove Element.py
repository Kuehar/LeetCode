class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        while val in nums:
            nums.remove(val)
        return len(nums)
# Runtime: 51 ms, faster than 28.39% of Python3 online submissions for Remove Element.
# Memory Usage: 14 MB, less than 97.02% of Python3 online submissions for Remove Element.
