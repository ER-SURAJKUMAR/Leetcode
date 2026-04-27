from collections import deque

class Solution:
    def hasValidPath(self, grid: list[list[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Directions: (row_offset, col_offset): [list of street types that can ENTER from this move]
        # For example, if we move Right (0, 1), the neighbor must be type 1, 3, or 5.
        directions = {
            (0, 1): {1, 3, 5},  # Moving Right
            (0, -1): {1, 4, 6}, # Moving Left
            (1, 0): {2, 5, 6},  # Moving Down
            (-1, 0): {2, 3, 4}  # Moving Up
        }
        
        # Mapping street types to the directions they can MOVE TOWARDS
        street_map = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }
        
        queue = deque([(0, 0)])
        visited = {(0, 0)}
        
        while queue:
            r, c = queue.popleft()
            
            if r == m - 1 and c == n - 1:
                return True
            
            # Check all possible exits from the current street type
            for dr, dc in street_map[grid[r][c]]:
                nr, nc = r + dr, c + dc
                
                # 1. Stay within bounds
                # 2. Not visited
                # 3. The neighbor must have a valid connection back to the current cell
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    if grid[nr][nc] in directions[(dr, dc)]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        
        return False