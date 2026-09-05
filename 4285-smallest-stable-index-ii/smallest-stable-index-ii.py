from typing import List

class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        suff_min = [0] * n
        suff_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suff_min[i] = min(suff_min[i + 1], nums[i])
            
        curr_max = float('-inf')
        for i in range(n):
            if nums[i] > curr_max:
                curr_max = nums[i]
            
            if curr_max - suff_min[i] <= k:
                return i
                
        return -1