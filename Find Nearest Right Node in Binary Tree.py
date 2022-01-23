# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        # BFSで走査すれば同じ深さ、かつ次のノードを見つけられる
        # 2つのdequeを用意し、cur_levelは現在の階層、next_levelでは一つ下の階層のノードを確認する
        if root is None:
            return []
        
        next_level = deque([root])
        while next_level:
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
# Runtime: 410 ms, faster than 40.94% of Python3 online submissions for Find Nearest Right Node in Binary Tree.
# Memory Usage: 51.6 MB, less than 74.50% of Python3 online submissions for Find Nearest Right Node in Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        # 番兵を使った方法。各レベルの終端に番兵としてnull(PythonのNone)を入れることで階層の管理を行う。
        if root is None:
            return []
        
        queue = deque([root,None])
        while queue:
            cur = queue.popleft()
            
            if cur == u:
                return queue.popleft()
            
            if cur:
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            else:
                if queue:
                    queue.append(None)
# Runtime: 342 ms, faster than 56.04% of Python3 online submissions for Find Nearest Right Node in Binary Tree.
# Memory Usage: 52.3 MB, less than 48.99% of Python3 online submissions for Find Nearest Right Node in Binary Tree.                    
