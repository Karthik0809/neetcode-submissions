class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Global variable to track the maximum sum found
        self.max_sum = float('-inf')
        
        def dfs(node):
            # Base case: empty node
            if not node:
                return 0
            
            # Get the max path sum going DOWN from left child
            # If negative, ignore it (use 0 instead)
            left_sum = max(0, dfs(node.left))
            
            # Get the max path sum going DOWN from right child
            # If negative, ignore it (use 0 instead)
            right_sum = max(0, dfs(node.right))
            
            # OPTION 1: Path that goes THROUGH this node
            # Connects left subtree → this node → right subtree
            path_through_node = left_sum + node.val + right_sum
            
            # Update global maximum
            self.max_sum = max(self.max_sum, path_through_node)
            
            # OPTION 2: Return the max path going DOWN
            # (can only go one direction to parent)
            return node.val + max(left_sum, right_sum)
        
        dfs(root)
        return self.max_sum