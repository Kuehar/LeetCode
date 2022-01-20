class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1
        mid = 0
        while right >= left:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
        return left
# Runtime: 90 ms, faster than 10.73% of Python3 online submissions for Search Insert Position.
# Memory Usage: 15 MB, less than 81.54% of Python3 online submissions for Search Insert Position.
