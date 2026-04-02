class Solution:
    def maximumAmount(self, coins: list[list[int]]) -> int:
        m, n = len(coins), len(coins[0])
        # Initialize DP table with negative infinity
        # dp[i][j][k] -> max coins at (i, j) with k neutralizations used
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]

        # Base case: Starting cell (0, 0)
        # 0 neutralizations used
        dp[0][0][0] = coins[0][0]
        # 1 neutralization used (only if it's a robber)
        if coins[0][0] < 0:
            dp[0][0][1] = 0
            # Note: dp[0][0][2] would also be 0, but 1 is sufficient/optimal
            dp[0][0][2] = 0 
        else:
            # If positive, using a neutralization is wasted, but technically 
            # the robot still has the coins.
            dp[0][0][1] = coins[0][0]
            dp[0][0][2] = coins[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                for k in range(3):
                    # Options to reach (i, j): from top or from left
                    res = -float('inf')
                    if i > 0:
                        res = max(res, dp[i-1][j][k])
                    if j > 0:
                        res = max(res, dp[i][j-1][k])
                    
                    # Option 1: Don't use a new neutralization at (i, j)
                    dp[i][j][k] = max(dp[i][j][k], res + coins[i][j])
                    
                    # Option 2: Use a neutralization at (i, j) if there's a robber
                    if k > 0 and coins[i][j] < 0:
                        prev_res = -float('inf')
                        if i > 0:
                            prev_res = max(prev_res, dp[i-1][j][k-1])
                        if j > 0:
                            prev_res = max(prev_res, dp[i][j-1][k-1])
                        
                        dp[i][j][k] = max(dp[i][j][k], prev_res) # Adding 0 coins

        return max(dp[m-1][n-1])