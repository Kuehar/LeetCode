# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans,level = [],0
        self.dfs(root,level,ans)
        return ans

    def dfs(self,root,level,ans):
        if not root:
            return
        if len(ans) < level+1:
            ans.append([])
        ans[level].append(root.val)
        self.dfs(root.left,level+1,ans)
        self.dfs(root.right,level+1,ans)
# Runtime: 32 ms, faster than 86.02% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 14.2 MB, less than 43.09% of Python3 online submissions for Binary Tree Level Order Traversal.
