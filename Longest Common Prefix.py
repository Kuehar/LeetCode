class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans = ""
        for num in zip(*strs):
            if len(set(num)) == 1:
               ans += num[0] 
            else:
                return ans
        return ans
# Runtime: 32 ms, faster than 74.42% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 14.1 MB, less than 22.07% of Python3 online submissions for Longest Common Prefix
