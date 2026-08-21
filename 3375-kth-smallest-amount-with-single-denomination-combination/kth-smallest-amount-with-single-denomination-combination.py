import math
from itertools import combinations

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        n = len(coins)
        
        # Precompute all non-empty subset LCMs with their inclusion-exclusion signs (+1 for odd sizes, -1 for even)
        subsets = []
        for r in range(1, n + 1):
            sign = 1 if r % 2 == 1 else -1
            for combo in combinations(coins, r):
                lcm_val = combo[0]
                for coin in combo[1:]:
                    lcm_val = (lcm_val * coin) // math.gcd(lcm_val, coin)
                subsets.append((lcm_val, sign))
        
        # Helper function: counts how many numbers <= val are multiples of at least one coin
        def count_multiples(val: int) -> int:
            total = 0
            for lcm_val, sign in subsets:
                total += sign * (val // lcm_val)
            return total

        # Binary Search for the kth smallest amount
        low = 1
        high = min(coins) * k
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if count_multiples(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans