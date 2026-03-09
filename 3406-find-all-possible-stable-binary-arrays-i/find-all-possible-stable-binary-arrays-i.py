class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        # dp[i][j][k] where k=0 means last element was 0, k=1 means last element was 1
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        # Base cases: filling only zeros or only ones within the limit
        for i in range(min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(min(one, limit) + 1):
            dp[0][j][1] = 1
            
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # Calculate dp[i][j][0]: ending with 0
                # It's the sum of the previous state ending in 0 and ending in 1
                # minus the invalid cases where we've exceeded the limit of 0s
                val0 = (dp[i-1][j][0] + dp[i-1][j][1])
                if i > limit:
                    val0 -= dp[i - limit - 1][j][1]
                dp[i][j][0] = val0 % MOD
                
                # Calculate dp[i][j][1]: ending with 1
                val1 = (dp[i][j-1][0] + dp[i][j-1][1])
                if j > limit:
                    val1 -= dp[i][j - limit - 1][0]
                dp[i][j][1] = val1 % MOD
                
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD