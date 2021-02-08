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

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for i in reversed(range(1,len(digits))):
            if digits[i] != 10:
                break
            digits[i] = 0
            digits[i-1] += 1
        else:
            if digits[0] == 10:
                digits[0] = 1
                digits.append(0)
        return digits
# Runtime: 28 ms, faster than 90.07% of Python3 online submissions for Plus One.
# Memory Usage: 14.3 MB, less than 50.47% of Python3 online submissions for Plus One.
