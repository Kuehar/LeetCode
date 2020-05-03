# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(cur:TreeNode,par:TreeNode,gra:TreeNode):
            if gra and gra.val % 2 == 0:
                self.ans += cur.val
            if cur.left:
                dfs(cur.left,cur,par)
            if cur.right:
                dfs(cur.right,cur,par)

        dfs(root,None,None)
        return self.ans
# Runtime: 92 ms, faster than 98.47% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
# Memory Usage: 17.3 MB, less than 100.00% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(cur:TreeNode,par:TreeNode,gra:TreeNode):
            if gra and gra.val % 2 == 0:
                nonlocal ans
                ans += cur.val
            if cur.left:
                dfs(cur.left,cur,par)
            if cur.right:
                dfs(cur.right,cur,par)
        ans = 0
        dfs(root,None,None)
        return ans
# Runtime: 92 ms, faster than 98.47% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
# Memory Usage: 17.3 MB, less than 100.00% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.