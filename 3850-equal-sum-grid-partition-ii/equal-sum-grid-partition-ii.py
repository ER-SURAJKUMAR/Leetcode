from collections import defaultdict

class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        row_sums = [sum(row) for row in grid]
        total_sum = sum(row_sums)
        
        col_sums = [0] * n
        for r in range(m):
            for c in range(n):
                col_sums[c] += grid[r][c]

        # Pre-map value positions to check connectivity quickly
        # val_map[value] = set of (r, c)
        val_map = defaultdict(list)
        for r in range(m):
            for c in range(n):
                val_map[grid[r][c]].append((r, c))

        def exists_valid_cell(r_start, r_end, c_start, c_end, target):
            if target <= 0 or target not in val_map:
                return False
            
            rows = r_end - r_start + 1
            cols = c_end - c_start + 1
            
            for r, c in val_map[target]:
                if r_start <= r <= r_end and c_start <= c <= c_end:
                    # Connectivity Check:
                    if rows == 1:
                        if c == c_start or c == c_end: return True
                    elif cols == 1:
                        if r == r_start or r == r_end: return True
                    else:
                        # In a 2D block (rows > 1 and cols > 1), 
                        # any single cell removal keeps it connected.
                        return True
            return False

        # 1. Horizontal Cuts
        top_sum = 0
        for r in range(m - 1):
            top_sum += row_sums[r]
            bottom_sum = total_sum - top_sum
            diff = abs(top_sum - bottom_sum)
            
            if diff == 0: return True
            if top_sum > bottom_sum:
                if exists_valid_cell(0, r, 0, n - 1, diff): return True
            else:
                if exists_valid_cell(r + 1, m - 1, 0, n - 1, diff): return True

        # 2. Vertical Cuts
        left_sum = 0
        for c in range(n - 1):
            left_sum += col_sums[c]
            right_sum = total_sum - left_sum
            diff = abs(left_sum - right_sum)
            
            if diff == 0: return True
            if left_sum > right_sum:
                if exists_valid_cell(0, m - 1, 0, c, diff): return True
            else:
                if exists_valid_cell(0, m - 1, c + 1, n - 1, diff): return True
                
        return False