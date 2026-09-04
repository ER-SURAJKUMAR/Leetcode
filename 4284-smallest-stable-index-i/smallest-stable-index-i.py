class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Precompute the minimums from the right side (i to n-1)
        min_right = [0] * n
        min_right[n - 1] = nums[-1]
        for i in range(n - 2, -1, -1):
            min_right[i] = min(nums[i], min_right[i + 1])
            
        curr_max = float('-inf')
        
        # Iterate to find the smallest stable index
        for i in range(n):
            curr_max = max(curr_max, nums[i])
            
            if curr_max - min_right[i] <= k:
                return i
                
        return -1