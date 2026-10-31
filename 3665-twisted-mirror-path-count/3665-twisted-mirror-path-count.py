class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # dp[c+1] stores [ways coming from top / moving down, ways coming from left / moving right]
        dp = [[0, 0] for _ in range(n + 1)]
        dp[1] = [1, 1]
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    dp[c + 1] = [dp[c + 1][1], dp[c][0]]
                else:
                    val = (dp[c + 1][1] + dp[c][0]) % MOD
                    dp[c + 1] = [val, val]
                    
        return dp[n][0]