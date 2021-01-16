class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i for i in s.upper() if i.isalnum()]
        return s == s[::-1]
# Runtime: 44 ms, faster than 77.48% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 15.9 MB, less than 19.21% of Python3 online submissions for Valid Palindrome.
