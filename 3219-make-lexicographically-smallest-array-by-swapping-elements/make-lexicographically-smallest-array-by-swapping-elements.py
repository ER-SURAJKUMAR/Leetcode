from collections import deque

class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        # Pair each value with its original index and sort by value
        sorted_pairs = sorted((val, idx) for idx, val in enumerate(nums))
        
        result = [0] * n
        
        # Group elements where adjacent sorted values differ by <= limit
        groups = []
        indices_groups = []
        
        current_group = []
        current_indices = []
        
        for val, idx in sorted_pairs:
            if not current_group or val - current_group[-1] <= limit:
                current_group.append(val)
                current_indices.append(idx)
            else:
                groups.append(current_group)
                indices_groups.append(current_indices)
                current_group = [val]
                current_indices = [idx]
                
        if current_group:
            groups.append(current_group)
            indices_groups.append(current_indices)
            
        # Reassign sorted values into sorted original indices for each group
        for val_group, idx_group in zip(groups, indices_groups):
            idx_group.sort()
            for val, orig_idx in zip(val_group, idx_group):
                result[orig_idx] = val
                
        return result