class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        
        # Pre-calculate sums for each row and each column
        row_sums = [0] * m
        col_sums = [0] * n
        
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1:
                    row_sums[r] += 1
                    col_sums[c] += 1
        
        special_count = 0
        
        # Check each cell to see if it meets the "special" criteria
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1:
                    # A cell is special if its row and column each contain only one '1'
                    if row_sums[r] == 1 and col_sums[c] == 1:
                        special_count += 1
                        
        return special_count