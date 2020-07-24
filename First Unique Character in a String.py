class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        print(count)
        for index,word in enumerate(s):
            if count[word] == 1:
                return index
        return -1
# Runtime: 96 ms, faster than  83.49%  of  Python3  online submissions for  First Unique Character in a String.
# Memory Usage: 14 MB, less than  34.96%  of  Python3  online submissions for  First Unique Character in a String.
