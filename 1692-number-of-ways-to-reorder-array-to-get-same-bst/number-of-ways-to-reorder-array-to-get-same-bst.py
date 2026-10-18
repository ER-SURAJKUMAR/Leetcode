import math
from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        def dfs(arr: List[int]) -> int:
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            
            # math.comb(n, k) computes n Choose k modulo arithmetic directly
            ways_to_interleave = math.comb(len(left) + len(right), len(left)) % MOD
            
            return (ways_to_interleave * dfs(left) * dfs(right)) % MOD
        
        # Subtract 1 because we exclude the original permutation
        return (dfs(nums) - 1) % MOD