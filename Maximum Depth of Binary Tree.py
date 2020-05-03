# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        stack = [(root,1)]

        while stack:
            root,length = stack.pop()
            if not root:
                return 0

            if length > depth:
                depth = length
            if root.right:
                stack.append((root.right,length + 1))
            if root.left:
                stack.append((root.left,length + 1))
        return depth
# Runtime: 40 ms, faster than 70.51% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 14.9 MB, less than 90.62% of Python3 online submissions for Maximum Depth of Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            curr, val = queue.popleft()
            if not curr.left and not curr.right and not queue:
                return val
            if curr.left:
                queue.append((curr.left, val+1))
            if curr.right:
                queue.append((curr.right, val+1))
# Runtime: 36 ms, faster than 89.87% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 15 MB, less than 90.62% of Python3 online submissions for Maximum Depth of Binary Tree.