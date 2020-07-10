class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pre = cur = 0
        while pre < len(s) and cur < len(t):
            if s[pre] == t[cur]:
                pre +=1
            cur +=1
        return pre == len(s)
# Runtime: 36 ms, faster than 60.46% of Python3 online submissions for Is Subsequence.
# Memory Usage: 14.1 MB, less than 35.95% of Python3 online submissions for Is Subsequence.
