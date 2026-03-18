class Solution:
    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        # We can use a 2D prefix sum approach
        # prefix_sum[i][j] will store the sum of submatrix from (0,0) to (i,j)
        prefix_sum = [[0] * cols for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                # Current value
                current_val = grid[r][c]
                
                # Add sum from above
                top = prefix_sum[r-1][c] if r > 0 else 0
                # Add sum from left
                left = prefix_sum[r][c-1] if c > 0 else 0
                # Subtract the diagonal overlap (added twice by top and left)
                overlap = prefix_sum[r-1][c-1] if (r > 0 and c > 0) else 0
                
                prefix_sum[r][c] = current_val + top + left - overlap
                
                # Check if the submatrix starting at (0,0) satisfies the condition
                if prefix_sum[r][c] <= k:
                    count += 1
                elif r > 0 and c == 0:
                    # Optimization: Since elements are non-negative, if a sum 
                    # in the first column exceeds k, further rows in this column 
                    # will also exceed k.
                    pass 
                    
        return count