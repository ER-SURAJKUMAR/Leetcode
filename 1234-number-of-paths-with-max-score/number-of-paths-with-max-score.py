class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        n = len(board)
        MOD = 10**9 + 7
        
        # dp[i][j] will store [max_sum, path_count]
        # Initialize with [-1, 0] to represent unreached/invalid states
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]
        
        # Base case: Starting at 'S' at the bottom-right corner
        dp[n-1][n-1] = [0, 1]
        
        # Iterate backwards from bottom-right to top-left
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Skip obstacles and the starting point (already initialized)
                if board[i][j] == 'X' or (i == n - 1 and j == n - 1):
                    continue
                
                max_sum = -1
                paths = 0
                
                # Check the three possible incoming directions (Down, Right, Down-Right)
                directions = [(i + 1, j), (i, j + 1), (i + 1, j + 1)]
                
                for ni, nj in directions:
                    if ni < n and nj < n and dp[ni][nj][0] != -1:
                        prev_sum, prev_paths = dp[ni][nj]
                        
                        if prev_sum > max_sum:
                            max_sum = prev_sum
                            paths = prev_paths
                        elif prev_sum == max_sum:
                            paths = (paths + prev_paths) % MOD
                
                # If at least one valid incoming path exists, update the current cell
                if max_sum != -1:
                    current_val = int(board[i][j]) if board[i][j] != 'E' else 0
                    dp[i][j] = [max_sum + current_val, paths]
        
        # The answer for reaching 'E' is at the top-left corner dp[0][0]
        result = dp[0][0]
        return [result[0], result[1]] if result[0] != -1 else [0, 0]