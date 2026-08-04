from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # ✅ STEP 1: Create queue with ALL treasures (0s)
        queue = deque()
        visited = set()
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:  # Treasure
                    queue.append((row, col, 0))  # (row, col, distance)
                    visited.add((row, col))
        
        # ✅ STEP 2: BFS from all treasures simultaneously
        while queue:
            row, col, distance = queue.popleft()
            
            # Explore 4 neighbors
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                
                # Check bounds and if not visited
                if (0 <= new_row < ROWS and 
                    0 <= new_col < COLS and 
                    (new_row, new_col) not in visited and
                    grid[new_row][new_col] != -1):  # Not obstacle
                    
                    # Update distance
                    grid[new_row][new_col] = distance + 1
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, distance + 1))