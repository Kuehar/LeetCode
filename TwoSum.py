"""
https://leetcode.com/problems/two-sum/submissions/
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            mid = target - nums[i]
            for j in range(i+1,len(nums)):
                if mid == nums[j]:
                    return [i,j]




    """
    Bruteforce solution
    Runtime:3436ms
    Memory:13.6MB
    This solution designed with bruteforce.it's more slowly method than others.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            mid = target - nums[i]
            for j in range(i+1,len(nums)):
                if mid == nums[j]:
                    return [i,j]

    """
    Hashmap solution
    Runtime:48ms
    Memory:14.1MB
    """
    def hashmap(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()

        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if num in hashmap:
                return [hashmap[num],i]
            else:
                hashmap[complement] = i
                
                
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                ans =  nums[i] + nums[j]
                if target == ans:
                    return [i,j]
# Runtime: 6848 ms, faster than 5.01% of Python3 online submissions for Two Sum.
# Memory Usage: 14.6 MB, less than 18.14% of Python3 online submissions for Two Sum.
