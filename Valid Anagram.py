class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list,t_list = list(s),list(t)
        s_list.sort()
        t_list.sort()
        return s_list == t_list
# Runtime: 48 ms, faster than 61.40% of Python3 online submissions for Valid Anagram.
# Memory Usage: 15 MB, less than 7.45% of Python3 online submissions for Valid Anagram.
