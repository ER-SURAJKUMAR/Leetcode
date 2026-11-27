from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_factor = max(f for f, _ in items)
        
        # Count occurrences of each factor
        freq = [0] * (max_factor + 1)
        for f, _ in items:
            freq[f] += 1
            
        # Precompute free copies gained by purchasing at least 1 copy of each factor
        free_by_factor = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            if freq[f] > 0:
                multiples = sum(freq[m] for m in range(f, max_factor + 1, f))
                free_by_factor[f] = multiples - 1
                
        # 0/1 Knapsack: dp[c] = max items from buying distinct item types with exact cost c
        dp = [-1] * (budget + 1)
        dp[0] = 0
        min_price = float('inf')
        
        for f, p in items:
            if p < min_price:
                min_price = p
            gain = 1 + free_by_factor[f]
            for c in range(budget, p - 1, -1):
                if dp[c - p] != -1:
                    if dp[c - p] + gain > dp[c]:
                        dp[c] = dp[c - p] + gain
                        
        # Spend any leftover budget on the single cheapest item available
        ans = 0
        for c in range(budget + 1):
            if dp[c] != -1:
                extra_copies = (budget - c) // min_price
                ans = max(ans, dp[c] + extra_copies)
                
        return ans