# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        stack = []
        stack.append((root,sum-root.val))
        while stack:
            node,sum = stack.pop()
            if not node.left and not node.right and sum == 0:
                return True
            if node.left:
                stack.append((node.left,sum-node.left.val))
            if node.right:
                stack.append((node.right,sum-node.right.val))       
        return False
# Runtime: 48 ms, faster than 55.07% of Python3 online submissions for Path Sum.
# Memory Usage: 15.6 MB, less than 52.21% of Python3 online submissions for Path Sum.
