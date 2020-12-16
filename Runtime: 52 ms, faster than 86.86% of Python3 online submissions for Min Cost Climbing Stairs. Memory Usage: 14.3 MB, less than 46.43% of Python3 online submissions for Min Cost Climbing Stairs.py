class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = reversed(cost)
        n1 = n2 = 0
        for c in cost:
            n1,n2 = c+min(n1,n2),n1
        return min(n1,n2)
# Runtime: 52 ms, faster than 86.86% of Python3 online submissions for Min Cost Climbing Stairs.
# Memory Usage: 14.3 MB, less than 46.43% of Python3 online submissions for Min Cost Climbing Stairs.
