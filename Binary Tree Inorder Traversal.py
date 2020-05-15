# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return 0
            right = dfs(node.right)
            left = dfs(node.left)
            self.ans = max(self.ans,left+right)
            return max(left,right) + 1

        dfs(root)
        return self.ans
# Runtime: 44 ms, faster than 72.73% of Python3 online submissions for Diameter of Binary Tree.
# Memory Usage: 15.9 MB, less than 51.72% of Python3 online submissions for Diameter of Binary Tree.
