# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base case 1: If subRoot is empty, it's always a subtree of any tree
        if not subRoot:
            return True
        
        # Base case 2: If root is empty but subRoot is not, can't be a subtree
        if not root:
            return False

        # Case 1: Check if current root node matches subRoot perfectly
        if self.sameTree(root, subRoot):
            return True
        
        # Case 2: If current node doesn't match, check left and right subtrees
        # subRoot might be in left subtree OR right subtree
        return (self.isSubtree(root.left, subRoot) or
               self.isSubtree(root.right, subRoot))

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """Helper function: Check if two trees are IDENTICAL"""
        
        # Both trees are empty → they're identical
        if not root and not subRoot:
            return True
        
        # Both nodes exist AND have same value
        if root and subRoot and root.val == subRoot.val:
            # Recursively check if left subtrees match AND right subtrees match
            return (self.sameTree(root.left, subRoot.left) and
                   self.sameTree(root.right, subRoot.right))
        
        # One exists and other doesn't, OR values don't match → not identical
        return False