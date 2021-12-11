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
# Time complexity: O(N).
# Space complexity: O(N).

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def minimum_cost(i):
            # ベースケース
            if i <= 1:
                return 0
            # 計算済みの内容が含まれていたらそちらを返す
            if i in memo:
                return memo[i]
            
            # 計算されていない部分の場合は計算し、ハッシュに保存する
            down_one = cost[i-1] + minimum_cost(i-1)
            down_two = cost[i-2] + minimum_cost(i-2)
            memo[i] = min(down_one,down_two)
            return memo[i]
        
        memo = {}
        return minimum_cost(len(cost))

# ↑の回答は以下のように書くこともできる 
# 注意!LeetCodeでは自動的にモジュールがインポートされるので大丈夫だが、本来であればインポートが必要
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def minimum_cost(i):
            if i <= 1:
                return 0
            
            down_one = cost[i - 1] + minimum_cost(i - 1)
            down_two = cost[i - 2] + minimum_cost(i - 2)
            return min(down_one, down_two)

        return minimum_cost(len(cost))
# Time complexity: O(N)
# Space complexity: O(N)
