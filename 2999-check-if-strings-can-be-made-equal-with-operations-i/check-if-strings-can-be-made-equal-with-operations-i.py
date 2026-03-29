class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # even1 holds characters at indices 0 and 2
        even1 = sorted([s1[0], s1[2]])
        # odd1 holds characters at indices 1 and 3
        odd1 = sorted([s1[1], s1[3]])
        
        # even2 holds characters at indices 0 and 2
        even2 = sorted([s2[0], s2[2]])
        # odd2 holds characters at indices 1 and 3
        odd2 = sorted([s2[1], s2[3]])
        
        # Returns True only if both parity groups match
        return even1 == even2 and odd1 == odd2