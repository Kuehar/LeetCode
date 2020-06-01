class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        for i in range(len(s),0,-1):
            for j in range(len(s)-i+1):
                if s[j:i+j] == s[j:i+j][::-1]:
                    return s[j:i+j]
# Runtime: 4884 ms, faster than 25.37% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 13.7 MB, less than 22.69% of Python3 online submissions for Longest Palindromic Substring.

class Solution(object):
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        start = 0
        maxLen = 1
        i = 0

        while i < len(s):
            l = i
            r = i
            while r < len(s) - 1 and s[r] == s[r+1]:
                r += 1
            i = r + 1
            while r < len(s)-1 and l > 0 and s[r+1] == s[l-1]:
                l -= 1
                r += 1
            if maxLen < r - l + 1:
                start = l
                maxLen = r - l + 1
        return s[start: start + maxLen]
# Runtime: 116 ms, faster than 95.05% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 13.8 MB, less than 22.69% of Python3 online submissions for Longest Palind
