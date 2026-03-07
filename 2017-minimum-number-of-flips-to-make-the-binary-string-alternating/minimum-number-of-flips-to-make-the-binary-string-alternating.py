class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        # Double the string to simulate all possible cyclic shifts via sliding window
        s = s + s
        
        # Target alternating patterns
        target1 = ""
        target2 = ""
        for i in range(len(s)):
            target1 += "0" if i % 2 == 0 else "1"
            target2 += "1" if i % 2 == 0 else "0"
            
        res = float('inf')
        diff1, diff2 = 0, 0
        l = 0
        
        for r in range(len(s)):
            # Increment differences if current char doesn't match targets
            if s[r] != target1[r]:
                diff1 += 1
            if s[r] != target2[r]:
                diff2 += 1
                
            # Once window size is n, start tracking results and sliding the left pointer
            if (r - l + 1) > n:
                if s[l] != target1[l]:
                    diff1 -= 1
                if s[l] != target2[l]:
                    diff2 -= 1
                l += 1
            
            # Update minimum flips when window is exactly length n
            if (r - l + 1) == n:
                res = min(res, diff1, diff2)
                
        return res