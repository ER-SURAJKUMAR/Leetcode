class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        # Precompute proper divisors for every possible substring length (up to n)
        divisors = [[] for _ in range(n + 1)]
        for length in range(2, n + 1):
            for d in range(1, length // 2 + 1):
                if length % d == 0:
                    divisors[length].append(d)
        
        # Helper to compute minimum changes needed to make s[i:j+1] a semi-palindrome
        def get_cost(i: int, j: int) -> int:
            length = j - i + 1
            min_changes = float('inf')
            
            for d in divisors[length]:
                changes = 0
                group_len = length // d
                # Check each of the d groups
                for rem in range(d):
                    left = i + rem
                    right = i + rem + (group_len - 1) * d
                    while left < right:
                        if s[left] != s[right]:
                            changes += 1
                        left += d
                        right -= d
                min_changes = min(min_changes, changes)
                
            return min_changes

        # cost[i][j] stores the min changes to turn s[i..j] into a semi-palindrome
        # Note: A valid semi-palindrome must have length >= 2
        cost = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                cost[i][j] = get_cost(i, j)
                
        # dp[parts][end] = min changes to partition s[0..end] into `parts` substrings
        dp = [[float('inf')] * n for _ in range(k + 1)]
        
        # Base case: 1 partition covering s[0..j]
        for j in range(1, n):
            dp[1][j] = cost[0][j]
            
        # Fill DP table for 2 to k partitions
        for parts in range(2, k + 1):
            # Minimum index needed to fit `parts` substrings of length >= 2 is 2 * parts - 1
            for j in range(2 * parts - 1, n):
                # Previous partition ends at `m`, new substring is s[m+1..j]
                for m in range(2 * (parts - 1) - 1, j - 1):
                    if dp[parts - 1][m] != float('inf'):
                        dp[parts][j] = min(dp[parts][j], dp[parts - 1][m] + cost[m + 1][j])
                        
        return dp[k][n - 1]