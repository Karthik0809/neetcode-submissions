# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Result list: each element is a list of values at that level
        res = []

        def dfs(node, depth):
            # Base case: empty node
            if not node:
                return None
            
            # If this is the first time visiting this depth level,
            # create a new list to store nodes at this level
            if len(res) == depth:
                res.append([])

            # Add current node's value to its level list
            res[depth].append(node.val)
            
            # Recursively visit left child (depth increases by 1)
            dfs(node.left, depth + 1)
            
            # Recursively visit right child (depth increases by 1)
            dfs(node.right, depth + 1)

        # Start DFS from root at depth 0
        dfs(root, 0)
        return res
        