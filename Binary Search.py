class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo,hi = 0,len(nums)-1
        while lo <= hi:
            mid = (hi+lo)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                lo = mid+1
            elif target < nums[mid]:
                hi = mid-1
        return -1
# Runtime: 430 ms, faster than 9.24% of Python3 online submissions for Binary Search.
# Memory Usage: 15.5 MB, less than 91.51% of Python3 online submissions for Binary Search.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
# Runtime: 342 ms, faster than 26.73% of Python3 online submissions for Binary Search. こっちの方が速い・・・
# Memory Usage: 15.7 MB, less than 30.42% of Python3 online submissions for Binary Search.
