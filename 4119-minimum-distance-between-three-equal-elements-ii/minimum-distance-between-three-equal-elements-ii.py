from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        # Map each value to a list of its indices
        index_map = defaultdict(list)
        for index, val in enumerate(nums):
            index_map[val].append(index)
        
        min_dist = float('inf')
        found = False
        
        # Iterate through values that appeared at least 3 times
        for val in index_map:
            indices = index_map[val]
            if len(indices) >= 3:
                found = True
                # Check consecutive triplets of indices for the same value
                # For i < j < k, distance = 2 * (k - i)
                for m in range(len(indices) - 2):
                    i = indices[m]
                    k = indices[m + 2]
                    current_dist = 2 * (k - i)
                    if current_dist < min_dist:
                        min_dist = current_dist
                        
        return min_dist if found else -1