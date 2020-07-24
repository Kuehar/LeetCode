class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(cur,left,num):
            if left == 0:
                ans.append(cur+[])
                return
            for i in range(num,len(candidates)):
                if left-candidates[i] >= 0:
                    cur.append(candidates[i])
                    dfs(cur,left-candidates[i],i)
                    cur.pop()
        dfs([],target,0)
        return ans
# Runtime: 84 ms, faster than 63.61% of Python3 online submissions for Combination Sum.
# Memory Usage: 14.1 MB, less than 11.55% of Python3 online submissions for Combination Sum.
