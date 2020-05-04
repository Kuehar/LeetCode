class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0]
        for i in range(1,num+1):
            tmp = ans[i//2] + (i%2)
            ans.append(tmp)
        return ans
# Runtime: 84 ms, faster than 72.90% of Python3 online submissions for Counting Bits.
# Memory Usage: 20.7 MB, less than 5.00% of Python3 online submissions for Counting Bits.