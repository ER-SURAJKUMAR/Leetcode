class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sums = set()

        for r in range(m):
            for c in range(n):
                # Every single cell is a rhombus of area 0
                sums.add(grid[r][c])
                
                # Try expanding the rhombus size (k is the distance to corners)
                k = 1
                while r + 2 * k < m and c - k >= 0 and c + k < n:
                    current_sum = 0
                    
                    # Top corner: (r, c)
                    # Bottom corner: (r + 2k, c)
                    # Left corner: (r + k, c - k)
                    # Right corner: (r + k, c + k)
                    
                    # Add the 4 corners
                    current_sum += grid[r][c]           # Top
                    current_sum += grid[r + 2 * k][c]   # Bottom
                    current_sum += grid[r + k][c - k]   # Left
                    current_sum += grid[r + k][c + k]   # Right
                    
                    # Add the edges (excluding the corners already added)
                    for i in range(1, k):
                        current_sum += grid[r + i][c + i]       # Top-Right edge
                        current_sum += grid[r + i][c - i]       # Top-Left edge
                        current_sum += grid[r + 2 * k - i][c + i] # Bottom-Right edge
                        current_sum += grid[r + 2 * k - i][c - i] # Bottom-Left edge
                    
                    sums.add(current_sum)
                    k += 1
                    
        # Return the biggest 3 distinct sums in descending order
        return sorted(list(sums), reverse=True)[:3]