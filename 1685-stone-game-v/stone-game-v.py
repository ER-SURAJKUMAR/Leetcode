from functools import cache

class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        
        # Build prefix sums for O(1) range sum lookups
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]
            
        def get_sum(i, j):
            return pref[j + 1] - pref[i]

        @cache
        def dp(i, j):
            # Base case: single stone remaining
            if i == j:
                return 0
            
            res = 0
            total = get_sum(i, j)
            left_sum = 0
            
            # Try all split points k (from i to j - 1)
            for k in range(i, j):
                left_sum += stoneValue[k]
                right_sum = total - left_sum
                
                if left_sum < right_sum:
                    res = max(res, left_sum + dp(i, k))
                elif left_sum > right_sum:
                    res = max(res, right_sum + dp(k + 1, j))
                else: # left_sum == right_sum
                    res = max(res, left_sum + max(dp(i, k), dp(k + 1, j)))
                    
            return res

        return dp(0, n - 1)