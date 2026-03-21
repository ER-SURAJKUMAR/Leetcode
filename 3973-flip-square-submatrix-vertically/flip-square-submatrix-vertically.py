class Solution:
    def reverseSubmatrix(self, grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
        # Calculate the number of row swaps needed (half the side length)
        for i in range(k // 2):
            # Row index from the top of the submatrix
            row1 = x + i
            # Corresponding row index from the bottom of the submatrix
            row2 = x + k - 1 - i
            
            # Swap elements in each column of the submatrix for these two rows
            for j in range(y, y + k):
                grid[row1][j], grid[row2][j] = grid[row2][j], grid[row1][j]
                
        return grid