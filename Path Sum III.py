# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(root,sums,start):
            if not root:
                return 0
            sums -= root.val
            if sums == 0:
                self.ans += 1
            dfs(root.left,sums,False)
            dfs(root.right,sums,False)
            if start:
                dfs(root.left,sum,True)
                dfs(root.right,sum,True)
        dfs(root,sum,True)
        return self.ans
# Runtime: 940 ms, faster than 24.67% of Python3 online submissions for Path Sum III.
# Memory Usage: 15.1 MB, less than 6.82% of Python3 online submissions for Path Sum III.
