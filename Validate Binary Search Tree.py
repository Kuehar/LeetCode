# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        low,high = float("-inf"),float("inf")
        def helper(node,low,high):
            if not node:
                return True
            val = node.val
            if val <= low or val >= high:
                return False
            
            if not helper(node.left,low,val):
                return False
            if not helper(node.right,val,high):
                return False
            return True
        return helper(root,low,high)
# Runtime: 44 ms, faster than  83.89%  of  Python3  online submissions for  Validate Binary Search Tree.
# Memory Usage: 16.2 MB, less than  43.01%  of  Python3  online submissions for  Validate Binary Search Tree.
