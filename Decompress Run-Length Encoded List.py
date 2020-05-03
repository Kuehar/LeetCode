class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0,len(nums),2):
            ans += [nums[i+1]]*nums[i]
        return ans
# Runtime: 60 ms, faster than 95.75% of Python3 online submissions for Decompress Run-Length Encoded List.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Decompress Run-Length Encoded List.

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(1,len(nums),2):
            ans += [nums[i]]*nums[i-1]
        return ans
# Runtime: 60 ms, faster than 95.75% of Python3 online submissions for Decompress Run-Length Encoded List.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Decompress Run-Length Encoded List.

class Solution:
    def decompressRLElist(self, A):
        return [x for a, b in zip(A[0::2], A[1::2]) for x in [b] * a]
# Runtime: 88 ms, faster than 5.86% of Python3 online submissions for Decompress Run-Length Encoded List.
# Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Decompress Run-Length Encoded List.