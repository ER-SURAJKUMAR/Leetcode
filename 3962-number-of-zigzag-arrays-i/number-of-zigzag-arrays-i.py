class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        K = r - l + 1
        
        # Flattened state representations to save memory allocation overhead
        # dp0: ending with a decreasing step
        # dp1: ending with an increasing step
        dp0 = [0] * (K + 2)
        dp1 = [0] * (K + 2)
        
        # Reusable arrays for next states to avoid allocating memory inside the loop
        next_dp0 = [0] * (K + 2)
        next_dp1 = [0] * (K + 2)
        
        # O(K) Initialization for length 2
        for curr in range(1, K + 1):
            dp1[curr] = curr - 1
            dp0[curr] = K - curr
                    
        # Main DP loop
        for length in range(3, n + 1):
            # 1. Compute prefix sums on the fly for dp0 (prev < curr)
            running_sum = 0
            for curr in range(1, K + 1):
                running_sum = (running_sum + dp0[curr - 1]) % MOD
                next_dp1[curr] = running_sum
                
            # 2. Compute suffix sums on the fly for dp1 (prev > curr)
            running_sum = 0
            for curr in range(K, 0, -1):
                running_sum = (running_sum + dp1[curr + 1]) % MOD
                next_dp0[curr] = running_sum
                
            # 3. Swap references instead of creating new arrays
            dp0, next_dp0 = next_dp0, dp0
            dp1, next_dp1 = next_dp1, dp1
            
        # Sum up all valid states
        total_valid = 0
        for j in range(1, K + 1):
            total_valid = (total_valid + dp0[j] + dp1[j]) % MOD
            
        return total_valid