# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None
        if original == target:
            return cloned

        return self.getTargetCopy(original.left,cloned.left,target) or self.getTargetCopy(original.right,cloned.right,target)
# Runtime: 672 ms, faster than 60.93% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
# Memory Usage: 23.5 MB, less than 100.00% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        que = collections.deque([(original, cloned)]) # start at the root
        while que:
            nodeOrig, nodeClon = que.popleft()
            if nodeOrig is target: # if original node is found - cloned node is our answer
                return nodeClon
            if nodeOrig.left:  que.append((nodeOrig.left, nodeClon.left))
            if nodeOrig.right: que.append((nodeOrig.right, nodeClon.right))
# Runtime: 656 ms, faster than 92.51% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
# Memory Usage: 23.6 MB, less than 100.00% of Python3 online submissions for Find a Corres
