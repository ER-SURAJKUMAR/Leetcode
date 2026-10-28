class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp[r][c] will store a set of all possible XOR path values to reach cell (r, c)
        dp = [[set() for _ in range(n)] for _ in range(m)]
        
        dp[0][0].add(grid[0][0])
        
        for r in range(m):
            for c in range(n):
                if not dp[r][c]:
                    continue
                current_xor_set = dp[r][c]
                
                # Move down
                if r + 1 < m:
                    for val in current_xor_set:
                        dp[r + 1][c].add(val ^ grid[r + 1][c])
                        
                # Move right
                if c + 1 < n:
                    for val in current_xor_set:
                        dp[r][c + 1].add(val ^ grid[r][c + 1])
                        
        return min(dp[m - 1][n - 1])