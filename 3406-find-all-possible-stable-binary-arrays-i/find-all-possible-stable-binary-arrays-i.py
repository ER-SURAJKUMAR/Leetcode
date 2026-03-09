from collections import deque

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10**9 + 7
        L = limit + 1

        # Previous row values
        dp0_prev, dp1_prev = [0] * (one + 1), [0] * (one + 1)
        
        # Initialize for the first row
        for j in range(1, min(one, limit) + 1):
            dp1_prev[j] = 1

        # We keep only the rows needed for the transition
        dp1q = deque([dp1_prev[:]])
        
        for i in range(1, zero + 1):
            dp0, dp1 = [0] * (one + 1), [0] * (one + 1)
            if i <= limit:
                dp0[0] = 1

            old1 = dp1q[0] if i >= L else None
            
            for j in range(1, one + 1):
                # Transition: Sum of prev row - the element that just slid out of the window
                dp0[j] = (dp0_prev[j] + dp1_prev[j] - (old1[j] if old1 is not None else 0)) % mod
                dp1[j] = (dp0[j - 1] + dp1[j - 1] - (dp0[j - L] if j >= L else 0)) % mod

            dp1q.append(dp1[:])
            if len(dp1q) > L:
                dp1q.popleft()

            dp0_prev, dp1_prev = dp0, dp1

        return (dp0_prev[one] + dp1_prev[one]) % mod