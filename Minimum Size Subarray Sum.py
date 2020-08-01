class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        index,num,low = 0,0,float("inf")
        for i in range(len(nums)):
            num += nums[i]
            while num >= s:
                low = min(low,i-index+1)
                num -= nums[index]
                index += 1
        return low if low != float("inf") else 0
# Runtime: 84 ms, faster than  56.50%  of  Python3  online submissions for  Minimum Size Subarray Sum.
# Memory Usage: 16.4 MB, less than  11.95%  of  Python3  online submissions for  Minimum Size Subarray Sum.
