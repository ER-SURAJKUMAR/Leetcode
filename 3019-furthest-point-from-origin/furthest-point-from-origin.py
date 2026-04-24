class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # Count occurrences of each character
        l_count = moves.count('L')
        r_count = moves.count('R')
        underscore_count = moves.count('_')
        
        # Calculate the net fixed distance and add all wildcards
        # to maximize the displacement in either direction.
        return abs(r_count - l_count) + underscore_count