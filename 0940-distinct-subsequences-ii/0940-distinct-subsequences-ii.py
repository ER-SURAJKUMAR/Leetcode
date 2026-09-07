class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        
        # dp[i] stores the number of distinct subsequences ending with the i-th letter of the alphabet
        dp = [0] * 26
        
        for char in s:
            char_idx = ord(char) - ord('a')
            
            # The new count of subsequences ending with 'char' becomes:
            # (Total count of all existing subsequences) + 1 (for the single character itself)
            dp[char_idx] = (sum(dp) + 1) % MOD
            
        # The answer is the sum of distinct subsequences ending across all possible characters
        return sum(dp) % MOD