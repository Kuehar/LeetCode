# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        prelevel = None
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if node:
                dfs(node.right)
                dfs(node.left)

                nonlocal prelevel
                node.right = prelevel
                node.left = None
                prelevel = node

        dfs(root)
# Runtime: 36 ms, faster than 74.14% of Python3 online submissions for Flatten Binary Tree to Linked List.
# Memory Usage: 14.6 MB, less than 8.70% of Python3 online submissions for Flatten Binary Tree to Linked List.     
