class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        n = len(colors)
        max_dist = 0
        
        # Scenario 1: Compare everything with the first house
        # We start from the end and move backwards to find the first different color
        for i in range(n - 1, 0, -1):
            if colors[i] != colors[0]:
                max_dist = max(max_dist, i)
                break
                
        # Scenario 2: Compare everything with the last house
        # We start from the beginning and move forward to find the first different color
        for i in range(n - 1):
            if colors[i] != colors[n - 1]:
                max_dist = max(max_dist, (n - 1) - i)
                break
                
        return max_dist