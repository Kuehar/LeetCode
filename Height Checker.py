class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        expected = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        return count
# Runtime: 36 ms, faster than 86.17% of Python3 online submissions for Height Checker.
# Memory Usage: 13.9 MB, less than 66.21% of Python3 online submissions for Height Checker.
