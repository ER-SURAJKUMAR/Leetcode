class Solution:
    def minMirrorPairDistance(self, nums: list[int]) -> int:
        # last_seen maps a value (that we want to find) to its most recent index
        # Key: reverse(nums[i]), Value: i
        last_seen = {}
        min_dist = float('inf')
        
        for j in range(len(nums)):
            current_val = nums[j]
            
            # 1. Check if the current number is a mirror of any previous index i
            # i.e., reverse(nums[i]) == current_val
            if current_val in last_seen:
                min_dist = min(min_dist, j - last_seen[current_val])
            
            # 2. Reverse current_val and store its index.
            # This allows a future nums[k] to check if reverse(nums[j]) == nums[k]
            reversed_val = int(str(current_val)[::-1])
            last_seen[reversed_val] = j
                
        return min_dist if min_dist != float('inf') else -1