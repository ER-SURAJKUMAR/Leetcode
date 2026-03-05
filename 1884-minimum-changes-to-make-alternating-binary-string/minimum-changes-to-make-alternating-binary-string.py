class Solution:
    def minOperations(self, s: str) -> int:
        res = 0
        n = len(s)
        
        # We count how many changes are needed to make the string 
        # match the pattern "010101..."
        for i in range(n):
            # In the "0101..." pattern:
            # Even indices (0, 2, 4...) should be '0'
            # Odd indices (1, 3, 5...) should be '1'
            if i % 2 == 0:
                if s[i] != '0':
                    res += 1
            else:
                if s[i] != '1':
                    res += 1
        
        # The number of changes to match "101010..." is (n - res)
        # We return the minimum of the two possible patterns
        return min(res, n - res)