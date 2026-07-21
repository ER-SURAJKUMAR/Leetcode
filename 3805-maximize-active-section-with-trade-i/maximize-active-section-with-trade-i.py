class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = "1" + s + "1"
        initial_ones = s.count('1')
        
        # Split t by '1's to get lengths of all contiguous '0' blocks
        zero_blocks = [len(b) for b in t.split('1') if b]
        
        # If there are fewer than 2 zero blocks, there is no internal block of '1's 
        # surrounded by '0's, so no valid trade can be performed.
        if len(zero_blocks) < 2:
            return initial_ones
        
        # A valid trade converts an internal block of '1's (between zero_blocks[i] and zero_blocks[i+1])
        # into '0's, merging them into a single contiguous block of '0's of length (zero_blocks[i] + zero_blocks[i+1]).
        # Then that merged block is converted to '1's.
        max_gain = max(zero_blocks[i] + zero_blocks[i + 1] for i in range(len(zero_blocks) - 1))
            
        return initial_ones + max_gain