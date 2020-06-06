class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = 0
        for i in range(1,len(nums)):
            if nums[n] < nums[i]:
                n += 1
                nums[n] = nums[i]
        return n+1
# Runtime: 84 ms, faster than 77.52% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 15.6 MB, less than 35.88% of Python3 online submissions for Remove Duplicates from Sorted Array.    
