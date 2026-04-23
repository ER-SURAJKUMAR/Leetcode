from typing import List
from collections import defaultdict

class Solution:
    # Rename this to 'distance' to match your driver's requirement
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        
        # Group indices by their value
        indices_map = defaultdict(list)
        for i, val in enumerate(nums):
            indices_map[val].append(i)
            
        for val in indices_map:
            indices = indices_map[val]
            m = len(indices)
            
            total_sum = sum(indices)
            prefix_sum = 0
            
            for i, idx in enumerate(indices):
                # Calculate sum of |idx - j|
                left_side = i * idx - prefix_sum
                
                right_sum = total_sum - prefix_sum - idx
                right_side = right_sum - (m - 1 - i) * idx
                
                res[idx] = left_side + right_side
                
                prefix_sum += idx
                
        return res