class Solution:
    def rotateGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        num_layers = min(m, n) // 2
        
        for layer in range(num_layers):
            # Define boundaries for the current layer
            top, left = layer, layer
            bottom, right = m - 1 - layer, n - 1 - layer
            
            # 1. Extract elements in counter-clockwise order
            elements = []
            
            # Top row: left to right (excluding last element to avoid corner overlap)
            for j in range(left, right):
                elements.append(grid[top][j])
            # Right col: top to bottom
            for i in range(top, bottom):
                elements.append(grid[i][right])
            # Bottom row: right to left
            for j in range(right, left, -1):
                elements.append(grid[bottom][j])
            # Left col: bottom to top
            for i in range(bottom, top, -1):
                elements.append(grid[i][left])
            
            # 2. Calculate effective rotations
            # k % len(elements) handles the large k constraint efficiently
            num_elements = len(elements)
            shift = k % num_elements
            
            # Perform the cyclic shift
            # In a CCW list, moving "forward" in the list is a CCW rotation
            rotated = elements[shift:] + elements[:shift]
            
            # 3. Place rotated elements back into the grid
            idx = 0
            for j in range(left, right):
                grid[top][j] = rotated[idx]
                idx += 1
            for i in range(top, bottom):
                grid[i][right] = rotated[idx]
                idx += 1
            for j in range(right, left, -1):
                grid[bottom][j] = rotated[idx]
                idx += 1
            for i in range(bottom, top, -1):
                grid[i][left] = rotated[idx]
                idx += 1
                
        return grid