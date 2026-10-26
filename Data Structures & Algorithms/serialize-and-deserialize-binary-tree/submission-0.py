# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        data = []
        def preorder_dfs(node):
            if node is None:
                data.append('#')
                return
            
            data.append(str(node.val))
            preorder_dfs(node.left)
            preorder_dfs(node.right)

        preorder_dfs(root)

        return ','.join(data)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(',')
        current = 0

        def dfs():
            nonlocal current
            if data[current] == '#':
                return None
            
            node = TreeNode(data[current])
            current += 1
            node.left = dfs()

            current += 1
            node.right = dfs()
            
            return node
        
        return dfs()