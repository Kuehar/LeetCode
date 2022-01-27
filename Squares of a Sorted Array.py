class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(x*x for x in nums)
# Runtime: 200 ms, faster than 98.52% of Python3 online submissions for Squares of a Sorted Array.
# Memory Usage: 16.3 MB, less than 31.98% of Python3 online submissions for Squares of a Sorted Array.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        left = 0
        right = n-1
        for i in range(n-1,-1,-1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            ans[i] = square * square
        return ans
# Runtime: 338 ms, faster than 30.27% of Python3 online submissions for Squares of a Sorted Array.
# Memory Usage: 16.1 MB, less than 75.08% of Python3 online submissions for Squares of a Sorted Array.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = sorted(nums, key=abs)
        ans = []
        for n in nums:
            ans.append(n*n)
        return ans
# Runtime: 345 ms, faster than 30.87% of Python3 online submissions for Squares of a Sorted Array.
# Memory Usage: 16.4 MB, less than 5.47% of Python3 online submissions for Squares of a Sorted Array.
