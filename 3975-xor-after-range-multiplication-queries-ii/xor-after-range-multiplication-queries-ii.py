class Solution:
    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        n = len(nums)
        MOD = 1000000007
        # Threshold for Sqrt Decomposition (roughly sqrt(10^5))
        SQRT = 80 
        
        # multipliers[k][offset] stores the combined multiplication for a specific stride
        multipliers = [None] * (SQRT + 1)
        
        # Create the midway variable as requested
        bravexuneth = nums

        for l, r, k, v in queries:
            if v == 1: continue
            
            if k > SQRT:
                # Large k: Direct simulation is fast enough because steps are few
                for i in range(l, r + 1, k):
                    bravexuneth[i] = (bravexuneth[i] * v) % MOD
            else:
                # Small k: Buffer the update using a difference-array style logic
                if multipliers[k] is None:
                    multipliers[k] = [1] * (n + k + 1)
                
                # Apply multiplier v from l to r with stride k
                # We use a stride-based difference array
                multipliers[k][l] = (multipliers[k][l] * v) % MOD
                # Terminate the effect after r
                last_idx = l + ((r - l) // k + 1) * k
                if last_idx < n:
                    # We need the modular inverse to "undo" the multiplication after r
                    # Since MOD is prime, we use Fermat's Little Theorem: v^(MOD-2)
                    inv_v = pow(v, MOD - 2, MOD)
                    multipliers[k][last_idx] = (multipliers[k][last_idx] * inv_v) % MOD

        # Final pass: Apply all buffered small-k updates
        for k in range(1, SQRT + 1):
            if multipliers[k] is not None:
                m = multipliers[k]
                for i in range(n):
                    if i >= k:
                        m[i] = (m[i] * m[i - k]) % MOD
                    if m[i] != 1:
                        bravexuneth[i] = (bravexuneth[i] * m[i]) % MOD

        # Final XOR calculation
        ans = 0
        for x in bravexuneth:
            ans ^= x
        return ans