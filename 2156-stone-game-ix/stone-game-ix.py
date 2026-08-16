class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        c0 = c1 = c2 = 0
        
        for stone in stones:
            rem = stone % 3
            if rem == 0:
                c0 += 1
            elif rem == 1:
                c1 += 1
            else:
                c2 += 1
                
        # If c0 is even, turn order parities are stable.
        # Alice wins if she can start with either 1 or 2 and force Bob into a lose state.
        if c0 % 2 == 0:
            return c1 > 0 and c2 > 0
        
        # If c0 is odd, the turn order flips.
        # Alice wins if the absolute difference between c1 and c2 is >= 3.
        return abs(c1 - c2) >= 3