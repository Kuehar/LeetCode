class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        if not s:
            return ans
        for i in range(len(s)):
            ans += 1 
            for j in range(1, i+1):
                if self.is_palindrom(s[i-j:i+1]):
                    ans += 1
        return ans

    def is_palindrom(self, s):
        return s == s[::-1]
# Runtime: 604 ms, faster than 13.54% of Python3 online submissions for Palindromic Substrings.
# Memory Usage: 13.8 MB, less than 81.86% of Python3 online submissions for Palindromic Substrings.
