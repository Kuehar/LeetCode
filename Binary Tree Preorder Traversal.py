# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        
        stack,output = [root,],[]
        
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
        return output
# Runtime: 28 ms, faster than 89.57% of Python3 online submissions for Binary Tree Preorder Traversal.
# Memory Usage: 14.3 MB, less than 12.87% of Python3 online submissions for Binary Tree Preorder Traversal.
