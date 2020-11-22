class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for s in ops:
            if s == "+":
                stack.append(stack[-1] + stack[-2])
            elif s == "C":
                stack.pop()
            elif s == "D":
                stack.append(stack[-1]*2)
            else:
                stack.append(int(s))
        return sum(stack)
# Runtime: 36 ms, faster than  83.92%  of  Python3  online submissions for  Baseball Game.
# Memory Usage: 14.2 MB, less than  92.17%  of  Python3  online submissions for  Baseball Game.
