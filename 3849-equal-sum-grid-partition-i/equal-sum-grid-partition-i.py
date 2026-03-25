class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        
        # Calculate total sum
        total_sum = sum(sum(row) for row in grid)
        
        # If total sum is odd, it's impossible to split into two equal integers
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        
        # 1. Check Horizontal Cuts
        # We sum up rows one by one
        current_horizontal_sum = 0
        for i in range(m - 1): # Up to m-1 to ensure non-empty sections
            current_horizontal_sum += sum(grid[i])
            if current_horizontal_sum == target:
                return True
                
        # 2. Check Vertical Cuts
        # We sum up columns one by one
        col_sums = [0] * n
        for r in range(m):
            for c in range(n):
                col_sums[c] += grid[r][c]
                
        current_vertical_sum = 0
        for j in range(n - 1): # Up to n-1 to ensure non-empty sections
            current_vertical_sum += col_sums[j]
            if current_vertical_sum == target:
                return True
                
        return False