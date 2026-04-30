class Solution:
    def maxPathScore(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp[i][j][c] stores the maximum score to reach cell (i, j) with cost exactly c.
        # Initializing with -1 to represent unreachable states.
        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]
        
        # Initial state at (0, 0). 
        # Per constraints, grid[0][0] is always 0 (score 0, cost 0).
        dp[0][0][0] = 0
        
        for i in range(m):
            for j in range(n):
                # Skip (0,0) as it is already initialized
                if i == 0 and j == 0:
                    continue
                
                val = grid[i][j]
                # Map cell values to score and cost
                cell_score = val # 0->0, 1->1, 2->2
                cell_cost = 1 if val > 0 else 0 # 0->0, 1->1, 2->1
                
                for c in range(cell_cost, k + 1):
                    # Check path from above
                    if i > 0 and dp[i-1][j][c - cell_cost] != -1:
                        dp[i][j][c] = max(dp[i][j][c], dp[i-1][j][c - cell_cost] + cell_score)
                    
                    # Check path from the left
                    if j > 0 and dp[i][j-1][c - cell_cost] != -1:
                        dp[i][j][c] = max(dp[i][j][c], dp[i][j-1][c - cell_cost] + cell_score)
                        
        # Get the maximum score at the bottom-right cell within cost k
        ans = max(dp[m-1][n-1])
        return ans if ans != -1 else -1