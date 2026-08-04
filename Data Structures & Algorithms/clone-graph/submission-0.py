"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # STEP 1: Create a visited map to track cloned nodes
        cloned = {}  # Maps original node → cloned node
        
        # STEP 2: DFS function
        def dfs(original_node):
            # Base case: Already cloned this node
            if original_node in cloned:
                return cloned[original_node]  # Return the clone
            
            # Create a clone of current node (without neighbors yet)
            clone_node = Node(original_node.val, [])
            
            # Mark as cloned (BEFORE recursing to handle cycles)
            cloned[original_node] = clone_node
            
            # Clone all neighbors
            for neighbor in original_node.neighbors:
                clone_node.neighbors.append(dfs(neighbor))
            
            return clone_node
        
        # STEP 3: Start DFS from the given node
        return dfs(node)
        
        