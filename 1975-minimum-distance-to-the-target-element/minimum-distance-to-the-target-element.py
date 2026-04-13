class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        # Initialize min_dist with a large value
        min_dist = float('inf')
        
        for i, num in enumerate(nums):
            if num == target:
                # Calculate the absolute difference
                current_dist = abs(i - start)
                
                # Update min_dist if the current distance is smaller
                if current_dist < min_dist:
                    min_dist = current_dist
                    
                # Optimization: if we find a distance of 0, it can't get smaller
                if min_dist == 0:
                    return 0
        
        return int(min_dist)