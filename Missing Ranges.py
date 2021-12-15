class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def formatRange(lower,upper):
            if lower == upper:
                return str(lower)
            return str(lower) + "->" + str(upper)
        
        ans = []
        prev = lower-1
        for i in range(len(nums)+1):
            curr = nums[i] if i < len(nums) else upper+1
            if prev+1 <= curr-1:
                ans.append(formatRange(prev+1,curr-1))
            prev = curr
        return ans
# Runtime: 35 ms, faster than 19.19% of Python3 online submissions for Missing Ranges.
# Memory Usage: 14.4 MB, less than 25.23% of Python3 online submissions for Missing Ranges.
