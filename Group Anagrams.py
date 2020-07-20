class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            sorted_word = ''.join(sorted(s))
            ans[sorted_word].append(s)
        return ans.values()
# Runtime: 92 ms, faster than 98.06% of Python3 online submissions for Group Anagrams.
# Memory Usage: 16.8 MB, less than 71.89% of Python3 online submissions for Group Anagrams.
