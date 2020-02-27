"""
https://leetcode.com/problems/two-sum/submissions/
This solving method designed with bruteforce.it's more slowly method than others.
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
