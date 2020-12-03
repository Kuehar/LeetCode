# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        val = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            val.append(node.val)
            dfs(node.right)
        dfs(root)
                
        tree = TreeNode(val[0])
        node = tree
        for i in range(1,len(val)):
            node.right = TreeNode(val[i])
            node = node.right
        return tree
# Runtime: 28 ms, faster than 83.05% of Python3 online submissions for Increasing Order Search Tree.
# Memory Usage: 14.4 MB, less than 6.40% of Python3 online submissions for Increasing Order Search Tree.
