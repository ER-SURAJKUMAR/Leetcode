class Solution:
    def maximumScore(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 0

        # Precompute column prefix sums for O(1) range queries
        col_sum = [[0] * (n + 1) for _ in range(n)]
        for c in range(n):
            for r in range(1, n + 1):
                col_sum[c][r] = col_sum[c][r - 1] + grid[r - 1][c]

        # dp[curr_h][prev_h] stores the max score for current state
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Helper arrays for optimized transitions
        # These store max scores seen in previous steps to avoid O(n^4)
        prev_max = [[0] * (n + 1) for _ in range(n + 1)]
        prev_suffix_max = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n):
            new_dp = [[0] * (n + 1) for _ in range(n + 1)]
            for curr_h in range(n + 1):
                for prev_h in range(n + 1):
                    if curr_h <= prev_h:
                        # Case: Current height is smaller/equal to previous
                        # Current column gains score from the previous column's height
                        extra = col_sum[i][prev_h] - col_sum[i][curr_h]
                        new_dp[curr_h][prev_h] = max(new_dp[curr_h][prev_h], 
                                                   prev_suffix_max[prev_h][0] + extra)
                    else:
                        # Case: Current height is larger than previous
                        # Previous column gains score from current column's height
                        extra = col_sum[i - 1][curr_h] - col_sum[i - 1][prev_h]
                        new_dp[curr_h][prev_h] = max(new_dp[curr_h][prev_h], 
                                                   prev_suffix_max[prev_h][curr_h],
                                                   prev_max[prev_h][curr_h] + extra)

            # Update the prefix/suffix max tables for the next column
            for curr_h in range(n + 1):
                # Calculate prefix max with penalty for the 'greater than' logic
                prev_max[curr_h][0] = new_dp[curr_h][0]
                for p_h in range(1, n + 1):
                    penalty = (col_sum[i][p_h] - col_sum[i][curr_h]) if p_h > curr_h else 0
                    prev_max[curr_h][p_h] = max(prev_max[curr_h][p_h - 1], 
                                               new_dp[curr_h][p_h] - penalty)

                # Calculate suffix max for the 'smaller than' logic
                prev_suffix_max[curr_h][n] = new_dp[curr_h][n]
                for p_h in range(n - 1, -1, -1):
                    prev_suffix_max[curr_h][p_h] = max(prev_suffix_max[curr_h][p_h + 1], 
                                                      new_dp[curr_h][p_h])
            dp = new_dp

        # The result is the maximum value in our final DP table
        ans = 0
        for k in range(n + 1):
            # We look at cases where the final column ends 'empty' or 'full' 
            # to capture all score possibilities from column n-1.
            ans = max(ans, dp[n][k], dp[0][k])

        return ans