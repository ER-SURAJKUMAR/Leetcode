class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        # Double the string to handle all Type-1 cyclic shifts
        s = s + s
        
        # We compare s against two patterns: 0101... and 1010...
        diff0, diff1 = 0, 0
        ans = float('inf')
        
        for i in range(len(s)):
            # Expected characters for the two alternating patterns
            # Pattern 0: 0, 1, 0, 1... (i % 2)
            # Pattern 1: 1, 0, 1, 0... (1 - i % 2)
            if int(s[i]) != (i % 2):
                diff0 += 1
            if int(s[i]) != (1 - i % 2):
                diff1 += 1
            
            # When the window exceeds size n, remove the element that fell out
            if i >= n:
                if int(s[i - n]) != ((i - n) % 2):
                    diff0 -= 1
                if int(s[i - n]) != (1 - (i - n) % 2):
                    diff1 -= 1
            
            # Start updating the answer once we have a full window of size n
            if i >= n - 1:
                ans = min(ans, diff0, diff1)
                
        return ans