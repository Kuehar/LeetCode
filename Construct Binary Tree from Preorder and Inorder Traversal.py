# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        preordersIndex = preorder[0]
        Tree = TreeNode(preordersIndex)
        inordersIndex = inorder.index(preordersIndex)

        Tree.left = self.buildTree(preorder[1:inordersIndex+1],inorder[:inordersIndex])
        Tree.right = self.buildTree(preorder[inordersIndex+1:],inorder[inordersIndex+1:])
        return Tree
# Runtime: 216 ms, faster than 33.07% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
# Memory Usage: 87.7 MB, less than 13.16% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root
# Runtime: 164 ms, faster than 49.71% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
# Memory Usage: 52.2 MB, less than 60.53% of Python3 online submissions for Construct Binary Tree fro
