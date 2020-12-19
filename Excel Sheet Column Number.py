class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for n in s:
            ans = ans*26 + ord(s) - ord('A') + 1
        return ans
# Runtime: 20 ms, faster than 99.34% of Python3 online submissions for Excel Sheet Column Number.
# Memory Usage: 14.2 MB, less than 48.32% of Python3 online submissions for Excel Sheet Column Number.
