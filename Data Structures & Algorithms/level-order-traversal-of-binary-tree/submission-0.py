# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS
        # use queue as frontier

        queue = deque()
        queue.append(root)
        res = []

        while queue:
            level = []
            # single level (clear the whole level)
            for _ in range(len(queue)):
                node = queue.popleft()
                if node is None:
                    continue
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            if level:
                res.append(level)
        
        return res

            
        