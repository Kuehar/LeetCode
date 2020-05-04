# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None
        if not t1:
            return t2
        if not t2:
            return t1
        if t1 and t2:
            ans = TreeNode(t1.val + t2.val)
            ans.left = self.mergeTrees(t1.left,t2.left)
            ans.right = self.mergeTrees(t1.right,t2.right)
            return ans
# Runtime: 92 ms, faster than 63.90% of Python3 online submissions for Merge Two Binary Trees.
# Memory Usage: 15.1 MB, less than 5.72% of Python3 online submissions for Merge Two Binary Trees.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        ans = TreeNode(t1.val + t2.val)
        ans.left = self.mergeTrees(t1.left,t2.left)
        ans.right = self.mergeTrees(t1.right,t2.right)
        return ans

# Runtime: 84 ms, faster than 94.01% of Python3 online submissions for Merge Two Binary Trees.
# Memory Usage: 14.9 MB, less than 5.72% of Python3 online submissions for Merge Two Binary Trees.