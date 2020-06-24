import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s,len_p,set_p,ans = len(s),len(p),Counter(p),[]
        for i in range(len_s-len_p+1):
            if Counter(s[i:i+len_p]) == set_p:
                ans.append(i)
        return ans
# Runtime: 7868 ms, faster than 7.31% of Python3 online submissions for Find All Anagrams in a String.
# Memory Usage: 14.8 MB, less than 69.94% of Python3 online submissions for Find All Anagrams in a String.
