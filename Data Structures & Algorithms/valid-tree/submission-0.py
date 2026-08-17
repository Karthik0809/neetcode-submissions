class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Check edge count first
        if len(edges) != n - 1:
            return False
        
        # Union-Find setup
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            
            # Cycle detected: both nodes already in same component
            if root_x == root_y:
                return False
            
            parent[root_x] = root_y
            return True
        
        # Try to union all edges
        for u, v in edges:
            if not union(u, v):  # Cycle found
                return False
        
        return True