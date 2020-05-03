# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        elif root.val < val:
            root.right =  self.insertIntoBST(root.right, val)
        return root
# Runtime: 124 ms, faster than 99.95% of Python3 online submissions for Insert into a Binary Search Tree.
# Memory Usage: 15.9 MB, less than 8.00% of Python3 online submissions for Insert into a Binary Search Tree.