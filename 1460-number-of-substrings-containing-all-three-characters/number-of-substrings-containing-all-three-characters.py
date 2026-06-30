class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {c: 0 for c in 'abc'}
        l = 0
        ans = 0
        n = len(s)
        
        for r in range(n):
            count[s[r]] += 1
            
            # While the window contains at least one 'a', 'b', and 'c'
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                # All substrings from index 'r' to the end of the string are valid
                ans += n - r
                
                # Shrink the window from the left
                count[s[l]] -= 1
                l += 1
                
        return ans