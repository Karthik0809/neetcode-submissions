class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """
        Convert tree to string.
        Use preorder traversal (Root → Left → Right)
        Mark null nodes with 'N'
        Separate values with ','
        """
        result = []
        
        def dfs(node):
            # Base case: null node
            if not node:
                result.append('N')  # Mark null
                return
            
            # Preorder: Process node FIRST
            result.append(str(node.val))  # Add node value
            
            # Then left subtree
            dfs(node.left)
            
            # Then right subtree
            dfs(node.right)
        
        dfs(root)
        
        # Join with comma: "1,2,N,N,3,N,N"
        return ','.join(result)
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        Rebuild tree from string.
        Use the same preorder order to reconstruct.
        """
        # Split string back into list
        values = data.split(',')
        
        # Use index to track position
        self.idx = 0
        
        def dfs():
            # Get current value
            val = values[self.idx]
            self.idx += 1
            
            # If null marker, return None
            if val == 'N':
                return None
            
            # Preorder: Create node FIRST
            node = TreeNode(int(val))
            
            # Then recursively build left
            node.left = dfs()
            
            # Then recursively build right
            node.right = dfs()
            
            return node
        
        return dfs()