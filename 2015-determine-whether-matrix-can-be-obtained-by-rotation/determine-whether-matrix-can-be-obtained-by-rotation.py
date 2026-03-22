class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        # Helper function to rotate the matrix 90 degrees clockwise
        def rotate(matrix):
            n = len(matrix)
            # Transpose the matrix
            for i in range(n):
                for j in range(i + 1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            # Reverse each row
            for i in range(n):
                matrix[i].reverse()
        
        # Check all 4 rotations (0, 90, 180, 270)
        for _ in range(4):
            if mat == target:
                return True
            rotate(mat)
            
        return False