class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        # The maximum value of a single subarray is achieved by taking 
        # the max element of the whole array minus the min element of the whole array.
        max_val = max(nums)
        min_val = min(nums)
        
        single_max_diff = max_val - min_val
        
        # We can greedily repeat this exact optimal subarray k times
        return single_max_diff * k