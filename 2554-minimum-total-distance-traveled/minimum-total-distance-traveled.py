class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        # Sort both to ensure the non-crossing property holds
        robot.sort()
        factory.sort()
        
        n, m = len(robot), len(factory)
        
        # dp[i][j] = min distance using first i factories to repair first j robots
        # Initialize with a very large value
        inf = float('inf')
        dp = [[inf] * (n + 1) for _ in range(m + 1)]
        
        # Base case: 0 robots repaired costs 0 distance
        for i in range(m + 1):
            dp[i][0] = 0
            
        for i in range(1, m + 1):
            f_pos, f_limit = factory[i-1]
            for j in range(n + 1):
                # Option 1: Current factory i repairs 0 robots
                dp[i][j] = dp[i-1][j]
                
                # Option 2: Current factory i repairs 'k' robots (1 <= k <= f_limit)
                dist_sum = 0
                for k in range(1, min(j, f_limit) + 1):
                    # Robot index is j-k
                    dist_sum += abs(robot[j-k] - f_pos)
                    
                    if dp[i-1][j-k] != inf:
                        dp[i][j] = min(dp[i][j], dp[i-1][j-k] + dist_sum)
                        
        return dp[m][n]