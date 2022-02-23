class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = left = right = count_zeros = 0
        while right < len(nums):
            if nums[right] == 0:
                count_zeros += 1
                
            while count_zeros == 2:
                if nums[left] == 0:
                    count_zeros -= 1
                left += 1
                
            ans = max(ans,right-left+1)
            right += 1
        return ans
# Runtime: 565 ms, faster than 40.93% of Python3 online submissions for Max Consecutive Ones II.
# Memory Usage: 14.2 MB, less than 98.51% of Python3 online submissions for Max Consecutive Ones II.
