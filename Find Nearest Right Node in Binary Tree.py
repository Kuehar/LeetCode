# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        # BFSで走査すれば同じ深さ、かつ次のノードを見つけられる
        if root is None:
            return []
        
        next_level = deque([root,])
        while next_level:
            print(next_level)
            cur_level = next_level
            next_level = deque()
            
            while cur_level:
                node = cur_level.popleft()
                
                if node == u:
                    return cur_level.popleft() if cur_level else None
                
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
