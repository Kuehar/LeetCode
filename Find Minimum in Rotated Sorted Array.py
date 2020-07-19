class Solution:
    def findMin(self, nums: List[int]) -> int:
        low,high = 0,len(nums)-1
        while low < high:
            mid = (high+low)//2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]
# Runtime: 36 ms, faster than 92.74% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 13.9 MB, less than 83.16% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
