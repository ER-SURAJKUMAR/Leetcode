class Solution:
    def containsCycle(self, grid: list[list[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c, pr, pc, char):
            visited.add((r, c))
            
            # Standard directions: Up, Down, Left, Right
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                
                # Check boundaries and character match
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == char:
                    # If neighbor is visited and not the parent, cycle found
                    if (nr, nc) in visited and (nr, nc) != (pr, pc):
                        return True
                    # If neighbor not visited, continue DFS
                    if (nr, nc) not in visited:
                        if dfs(nr, nc, r, c, char):
                            return True
            return False

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited:
                    # Start DFS; parent of start is (-1, -1)
                    if dfs(r, c, -1, -1, grid[r][c]):
                        return True
        
        return False