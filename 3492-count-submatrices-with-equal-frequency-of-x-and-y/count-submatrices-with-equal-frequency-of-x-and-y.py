class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        # 2D prefix sums for 'X' and 'Y'
        # preX[i][j] stores count of 'X' in grid[0...i-1][0...j-1]
        preX = [[0] * (cols + 1) for _ in range(rows + 1)]
        preY = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        count = 0
        
        for r in range(rows):
            for c in range(cols):
                # Calculate prefix sums for 'X'
                preX[r + 1][c + 1] = preX[r][c + 1] + preX[r + 1][c] - preX[r][c] + (1 if grid[r][c] == 'X' else 0)
                
                # Calculate prefix sums for 'Y'
                preY[r + 1][c + 1] = preY[r][c + 1] + preY[r + 1][c] - preY[r][c] + (1 if grid[r][c] == 'Y' else 0)
                
                # Current X and Y counts for submatrix (0,0) to (r,c)
                currX = preX[r + 1][c + 1]
                currY = preY[r + 1][c + 1]
                
                # Check conditions: equal frequency and at least one 'X'
                if currX > 0 and currX == currY:
                    count += 1
                    
        return count