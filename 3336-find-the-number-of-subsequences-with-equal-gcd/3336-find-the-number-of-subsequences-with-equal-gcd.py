import math

class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        max_num = max(nums)
        
        # dp[(x, y)] stores the number of ways to have 
        # gcd(seq1) = x and gcd(seq2) = y
        dp = {(0, 0): 1}
        
        for num in nums:
            next_dp = dp.copy()
            
            for (x, y), count in dp.items():
                # Choice 1: Put 'num' into seq1
                nx = num if x == 0 else math.gcd(x, num)
                next_dp[(nx, y)] = (next_dp.get((nx, y), 0) + count) % MOD
                
                # Choice 2: Put 'num' into seq2
                ny = num if y == 0 else math.gcd(y, num)
                next_dp[(x, ny)] = (next_dp.get((x, ny), 0) + count) % MOD
                
                # Choice 3: Skip 'num' (already handled by next_dp = dp.copy())
                
            dp = next_dp
            
        # Sum up all valid pairs where x == y and they are non-empty (x > 0)
        ans = 0
        for (x, y), count in dp.items():
            if x == y and x > 0:
                ans = (ans + count) % MOD
                
        return ans