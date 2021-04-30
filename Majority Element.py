from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans =  collections.Counter(nums)
        return ans.most_common(1)[0][0]
# Runtime: 172 ms, faster than 79.63% of Python3 online submissions for Majority Element.
# Memory Usage: 15.1 MB, less than 7.14% of Python3 online submissions for Majority Element.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return max(cnt.keys(),key=cnt.get)
