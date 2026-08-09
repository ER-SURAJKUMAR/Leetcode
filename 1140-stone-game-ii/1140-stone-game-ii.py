from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        
        # Calculate suffix sums to easily get total remaining stones from index i
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        @lru_cache(None)
        def dp(i: int, M: int) -> int:
            # If we can take all remaining piles at once, take them all
            if i + 2 * M >= n:
                return suffix_sum[i]
            
            max_stones = 0
            # Try taking X piles where 1 <= X <= 2 * M
            for X in range(1, 2 * M + 1):
                # Maximize current player's score by minimizing opponent's score
                current_take = suffix_sum[i] - dp(i + X, max(M, X))
                max_stones = max(max_stones, current_take)
                
            return max_stones
        
        return dp(0, 1)