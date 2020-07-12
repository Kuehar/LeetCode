class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        num,step,ans = 0,0,['']*numRows
        for w in s:
            ans[num] += w
            if num == 0:
                step = 1
            elif num == numRows - 1:
                step = -1
            num += step
        return "".join(ans)
# Runtime: 64 ms, faster than 65.13% of Python3 online submissions for ZigZag Conversion.
# Memory Usage: 14.1 MB, less than 10.13% of Python3 online submissions for ZigZag Conversion.
