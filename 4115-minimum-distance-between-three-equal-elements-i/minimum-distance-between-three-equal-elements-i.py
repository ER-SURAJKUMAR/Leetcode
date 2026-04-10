class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        from collections import defaultdict
        
        # Store the indices of each number
        indices_map = defaultdict(list)
        for index, value in enumerate(nums):
            indices_map[value].append(index)
            
        min_dist = float('inf')
        found = False
        
        # Iterate through the lists of indices for each number
        for value in indices_map:
            indices = indices_map[value]
            
            # A good tuple requires at least 3 distinct indices
            if len(indices) >= 3:
                found = True
                # To minimize 2 * (indices[k] - indices[i]),
                # check triplets of indices. Since the indices are 
                # appended in order, we only need to compare indices[i] and indices[i+2].
                for i in range(len(indices) - 2):
                    # Simplified distance: abs(i-j) + abs(j-k) + abs(k-i) = 2 * (max_idx - min_idx)
                    dist = 2 * (indices[i+2] - indices[i])
                    if dist < min_dist:
                        min_dist = dist
                    
        return int(min_dist) if found else -1