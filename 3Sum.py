class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1

            while left < right:
                sums = nums[i]+nums[left]+nums[right]
                if sums < 0:
                    left += 1
                elif sums > 0:
                    right -= 1
                else:
                    ans.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left]==nums[left+1]:
                        left += 1
                    while left > right and nums[right]==nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1  
        return ans
# Runtime: 1092 ms, faster than 45.79% of Python3 online submissions for 3Sum.
# Memory Usage: 17.1 MB, less than 76.15% of Python3 online submissions for 3Sum.
# While Solution
