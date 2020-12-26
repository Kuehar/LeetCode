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

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            else:
                s.add(num)
        return False
# Runtime: 116 ms, faster than 70.88% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 20.3 MB, less than 39.65% of Python3 online submissions for Contains Duplicate.
