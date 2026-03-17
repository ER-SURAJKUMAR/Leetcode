class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_area = 0
        
        # heights will store the number of consecutive 1s ending at the current row
        heights = [0] * n
        
        for i in range(m):
            for j in range(n):
                # Update the height of the column at row i
                if matrix[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            # Create a copy and sort heights to find the best submatrix for this row
            # Sorting descending allows us to greedily pick the largest widths
            current_row_heights = sorted(heights, reverse=True)
            
            for k in range(n):
                # Width is (k + 1), height is current_row_heights[k]
                area = current_row_heights[k] * (k + 1)
                max_area = max(max_area, area)
                
        return max_area