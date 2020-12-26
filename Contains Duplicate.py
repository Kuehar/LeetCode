class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l = sorted(nums)
        for i in range(len(nums)-1):
            print(i)
            if l[i] == l[i+1]:
                return True
        return False
# Runtime: 144 ms, faster than 5.87% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 19.6 MB, less than 83.37% of Python3 online submissions for Contains Duplicate.
