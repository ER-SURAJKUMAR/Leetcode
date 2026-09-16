import math

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # Total items to choose from: n + k - 1
        # Number of endpoints needed: 2 * k
        N = n + k - 1
        R = 2 * k
        
        if R > N:
            return 0
            
        return math.comb(N, R) % MOD