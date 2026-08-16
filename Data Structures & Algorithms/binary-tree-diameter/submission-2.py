class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Global variable to track the maximum diameter found
        res = 0

        def dfs(root):
            nonlocal res

            # Base case: empty node has height 0
            if not root:
                return 0
            
            # Recursively get the height of left and right subtrees
            left = dfs(root.left)
            right = dfs(root.right)
            
            # Update the global max diameter
            # Diameter through this node = left height + right height
            res = max(res, left + right)

            # Return the height of this subtree for parent calculation
            # Height = 1 (current node) + max height of children
            return 1 + max(left, right)

        dfs(root)
        return res



            


            

        

        
        
        