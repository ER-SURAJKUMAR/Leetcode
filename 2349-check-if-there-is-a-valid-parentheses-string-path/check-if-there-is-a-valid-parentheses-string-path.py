from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # A valid parentheses string must have an even length
        if (m + n - 1) % 2 != 0:
            return False
        
        # Must start with '(' and end with ')'
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False
            
        # dp[j] will store an integer bitmask representing all reachable balances for the current cell.
        # k-th bit set to 1 means a balance of k is possible.
        dp = [0] * n
        
        # Base case: start at (0,0) with balance 1.
        dp[0] = 1 << 1  
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                    
                # Combine all valid incoming balances from Top and Left
                mask = 0
                if i > 0:
                    mask |= dp[j]
                if j > 0:
                    mask |= dp[j-1]
                    
                if grid[i][j] == '(':
                    # All balances increase by 1 -> Shift bits left
                    dp[j] = mask << 1
                else:
                    # All balances decrease by 1 -> Shift bits right.
                    # This natively drops balances that go below 0 (since bit 0 shifted right disappears)
                    dp[j] = mask >> 1
                    
        # Check if bit 0 is set at the end (meaning a final balance of 0 is possible)
        return bool(dp[-1] & 1)