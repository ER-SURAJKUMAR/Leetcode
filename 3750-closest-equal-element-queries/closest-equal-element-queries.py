import bisect

class Solution:
    def solveQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        n = len(nums)
        # Map value to a sorted list of its indices
        pos_map = {}
        for i, val in enumerate(nums):
            if val not in pos_map:
                pos_map[val] = []
            pos_map[val].append(i)
        
        results = []
        
        for q_idx in queries:
            val = nums[q_idx]
            indices = pos_map[val]
            
            # If the number only appears once, no other index exists
            if len(indices) == 1:
                results.append(-1)
                continue
            
            # Find the position of the current query index in the sorted list
            pos = bisect.bisect_left(indices, q_idx)
            
            min_dist = float('inf')
            
            # We only need to check the immediate neighbors in the sorted list.
            # Due to the circular nature, the "left" of the first element is the last.
            
            # Check the neighbor to the left
            left_idx = indices[(pos - 1) % len(indices)]
            d1 = abs(q_idx - left_idx)
            dist_left = min(d1, n - d1)
            
            # Check the neighbor to the right
            right_idx = indices[(pos + 1) % len(indices)]
            d2 = abs(q_idx - right_idx)
            dist_right = min(d2, n - d2)
            
            results.append(min(dist_left, dist_right))
            
        return results