class Solution:
def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.dfs(root.left,root.right)
    
    def dfs(self,left,right):
        if left and right:
            return left.val == right.val and self.dfs(left.left,right.right) and self.dfs(left.right,right.left)
        else:
            return left == right
# Runtime: 32 ms, faster than 71.25% of Python3 online submissions for Symmetric Tree.
# Memory Usage: 13.9 MB, less than 5.17% of Python3 online submissions for Symmetric Tree.
