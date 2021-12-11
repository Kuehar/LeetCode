class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [inf]*(len(cost))
        dp[0] = cost[0]
        if len(cost) >= 2:
            dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[-1],dp[-2])
# Runtime: 56 ms, faster than 78.97% of Python3 online submissions for Min Cost Climbing Stairs.
# Memory Usage: 14.5 MB, less than 46.19% of Python3 online submissions for Min Cost Climbing Stairs.

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [inf]*len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,len(cost)):
            dp[i] = min(dp[i-1]+cost[i],dp[i-2]+cost[i])
        print(dp)
        return min(dp[-1],dp[-2])
# Runtime: 44 ms
# Memory Usage: 14.3 MB
