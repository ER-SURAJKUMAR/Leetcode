class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        total_elements = m * n
        
        # Optimize k to avoid unnecessary full rotations
        k = k % total_elements
        if k == 0:
            return grid
            
        # Flatten the 2D grid into a 1D list
        flattened = []
        for row in grid:
            flattened.extend(row)
            
        # Rotate the 1D list to the right by k
        # The last k elements come to the front, followed by the rest
        rotated = flattened[-k:] + flattened[:-k]
        
        # Reshape the 1D list back into a 2D grid
        result = []
        for i in range(0, total_elements, n):
            result.append(rotated[i : i + n])
            
        return result