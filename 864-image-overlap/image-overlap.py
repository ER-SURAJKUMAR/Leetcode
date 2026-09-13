from collections import Counter
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        # Collect coordinates of all 1s in both images
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        # Count frequency of each translation vector (dr, dc)
        overlap_counts = Counter()
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                dr = r2 - r1
                dc = c2 - c1
                overlap_counts[(dr, dc)] += 1
                
        # Return the maximum overlapping 1s for any translation vector
        return max(overlap_counts.values()) if overlap_counts else 0