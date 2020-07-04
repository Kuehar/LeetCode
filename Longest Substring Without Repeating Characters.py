class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic,length,start = {},0,0
        for i,j in enumerate(s):
            if j in dic:
                sums = dic[j] + 1
                if sums > start:
                    start = sums
            num = i - start + 1
            if num > length:
                length = num
            dic[j] = i
        return length
# Runtime: 60 ms, faster than 76.33% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 13.9 MB, less than 55.58% of Python3 online submissions for Longest Substring Without Repeating Characters.
