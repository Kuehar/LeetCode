# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        return root
# Runtime: 28 ms, faster than 74.30% of Python3 online submissions for Invert Binary Tree.
# Memory Usage: 13.8 MB, less than 5.41% of Python3 online submissions for Invert Binary Tree.