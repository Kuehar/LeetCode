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

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = [0]*128
        left = right = res = 0
        while right < len(s):
            r = s[right]
            char[ord(r)] += 1
            
            while char[ord(r)] > 1:
                l = s[left]
                char[ord(l)] -= 1
                left += 1
                
            res = max(res,right-left+1)
            
            
            right += 1
        return res
# Runtime: 131 ms, faster than 26.07% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.3 MB, less than 54.91% of Python3 online submissions for Longest Substring Without Repeating Characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        mp = {}
        i = 0
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]],i)
                
            ans = max(ans,j-i+1)
            mp[s[j]] = j +1
        return ans
# Runtime: 94 ms, faster than 53.46% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14 MB, less than 97.46% of Python3 online submissions for Longest Substring Without Repeating Characters.
