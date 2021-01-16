class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        elif digits[0] == 9 and len(digits) == 1:
            return [1,0]
        else:
            digits[-1] = 0
            digits[0:-1] = self.plusOne(digits[0:-1])
            return digits
# Runtime: 28 ms, faster than 88.73% of Python3 online submissions for Plus One.
# Memory Usage: 14.2 MB, less than 45.95% of Python3 online submissions for Plus One.
