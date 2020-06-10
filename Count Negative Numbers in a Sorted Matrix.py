import itertools

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        lists = []
        lists = list(itertools.chain.from_iterable(grid))
        for i in lists:
            if i < 0:
                count += 1
        return count
# Runtime: 128 ms, faster than 63.80% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
# Memory Usage: 14.9 MB, less than 20.02% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
