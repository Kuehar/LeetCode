class Solution(object):
    def dailyTemperatures(self, T):
        ans,stack, = [0] * len(T),[]
        for i, j in enumerate(T):
            while stack and T[stack[-1]] < j:
                ans[stack.pop()] = i - stack[-1]
            stack.append(i)
        return ans
# Runtime: 548 ms, faster than 32.01% of Python3 online submissions for Daily Temperatures.
# Memory Usage: 17.1 MB, less than 95.07% of Python3 online submissions for Daily Temperatures.
