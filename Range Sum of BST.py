# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if R > node.val:
                    dfs(node.right)
        self.ans = 0
        dfs(root)
        return self.ans
# Runtime: 224 ms, faster than 82.22% of Python3 online submissions for Range Sum of BST.
# Memory Usage: 21.9 MB, less than 7.92% of Python3 online submissions for Range Sum of BST.

class Soluion:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        elif root.val < L:
            return self.rangeSumBST(root.right, L, R)
        elif root.val > R:
            return self.rangeSumBST(root.left, L, R)
        return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
# Runtime: 244 ms, faster than 47.97% of Python3 online submissions for Range Sum of BST.
# Memory Usage: 22.1 MB, less than 5.94% of Python3 online submissions for Range Sum of BST.

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(root):
            if not root:
                return 0
            if root:
                if L <= root.val <= R:
                    self.ans += root.val
                if L < root.val:
                    dfs(root.left)
                if R > root.val:
                    dfs(root.right)
                    
            return self.ans
        self.ans = 0
        return dfs(root)
