class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i][j][0] -> stable arrays with i zeros, j ones, ending in 0
        # dp[i][j][1] -> stable arrays with i zeros, j ones, ending in 1
        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]
        
        # Base cases: single blocks within the limit
        for i in range(1, min(zero, limit) + 1):
            dp0[i][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp1[0][j] = 1
            
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # Transitions for dp0[i][j]:
                # We add a 0 to an array ending in 1.
                # dp0[i][j] = sum(dp1[i-k][j] for k in 1..limit)
                dp0[i][j] = (dp0[i-1][j] + dp1[i-1][j]) % MOD
                if i > limit:
                    # Subtract the case where we'd exceed the limit of consecutive 0s
                    dp0[i][j] = (dp0[i][j] - dp1[i-limit-1][j] + MOD) % MOD
                
                # Transitions for dp1[i][j]:
                # We add a 1 to an array ending in 0.
                # dp1[i][j] = sum(dp0[i][j-k] for k in 1..limit)
                dp1[i][j] = (dp1[i][j-1] + dp0[i][j-1]) % MOD
                if j > limit:
                    # Subtract the case where we'd exceed the limit of consecutive 1s
                    dp1[i][j] = (dp1[i][j] - dp0[i][j-limit-1] + MOD) % MOD
                    
        return (dp0[zero][one] + dp1[zero][one]) % MOD