class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # If t is longer than s, it's impossible to form t
        if n > m:
            return 0
        
        # dp[j] stores the number of distinct subsequences forming t[:j]
        dp = [0] * (n + 1)
        
        # An empty string t can always be formed in exactly 1 way
        dp[0] = 1
        
        for i in range(1, m + 1):
            # Traverse backwards to prevent overwriting the current row's previous states
            for j in range(n, 0, -1):
                # If characters match, we can either use the character or ignore it
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
                    
        return dp[n]