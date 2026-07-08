class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7
        m = len(s)
        
        # Extract non-zero digits
        A = [int(c) for c in s if c != '0']
        n = len(A)
        
        # Precompute mapping from original string indices to non-zero array indices
        next_nz = [n] * m
        prev_nz = [-1] * m
        
        # Fill next_nz (from right to left)
        curr = n
        for i in range(m - 1, -1, -1):
            if s[i] != '0':
                curr -= 1
            next_nz[i] = curr
            
        # Fill prev_nz (from left to right)
        curr = -1
        for i in range(m):
            if s[i] != '0':
                curr += 1
            prev_nz[i] = curr
            
        # Precompute prefix sums and prefix hashes for A
        P = [0] * (n + 1)  # Prefix hash
        S = [0] * (n + 1)  # Prefix sum
        pow10 = [1] * (n + 1)
        
        for i in range(n):
            P[i + 1] = (P[i] * 10 + A[i]) % MOD
            S[i + 1] = S[i] + A[i]
            pow10[i + 1] = (pow10[i] * 10) % MOD
            
        ans = []
        for l, r in queries:
            i = next_nz[l]
            j = prev_nz[r]
            
            # If there are no non-zero digits in the range s[l..r]
            if i > j:
                ans.append(0)
            else:
                # Length of the non-zero segment
                length = j - i + 1
                
                # Extract x % MOD using prefix hash
                x = (P[j + 1] - P[i] * pow10[length]) % MOD
                
                # Extract digit sum using prefix sum
                digit_sum = S[j + 1] - S[i]
                
                # Calculate final answer for the query
                ans.append((x * digit_sum) % MOD)
                
        return ans