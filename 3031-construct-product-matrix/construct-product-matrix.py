class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        MOD = 12345
        
        # Initialize the result matrix p
        p = [[0] * m for _ in range(n)]
        
        # Step 1: Forward pass for Prefix Products
        running_prod = 1
        for i in range(n):
            for j in range(m):
                p[i][j] = running_prod
                running_prod = (running_prod * (grid[i][j] % MOD)) % MOD
        
        # Step 2: Backward pass for Suffix Products
        running_prod = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                # Multiply the existing prefix product by the current suffix product
                p[i][j] = (p[i][j] * running_prod) % MOD
                # Update the running suffix product
                running_prod = (running_prod * (grid[i][j] % MOD)) % MOD
                
        return p