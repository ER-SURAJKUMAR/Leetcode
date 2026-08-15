class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        total_xor = 0
        has_non_zero = False
        
        for num in nums:
            total_xor ^= num
            if num != 0:
                has_non_zero = True
                
        # If all elements are 0, no non-zero XOR subsequence exists
        if not has_non_zero:
            return 0
            
        # If the total XOR of the array is non-zero, the whole array works
        if total_xor != 0:
            return len(nums)
            
        # If total XOR is 0, removing any 1 non-zero element leaves a non-zero XOR sum
        return len(nums) - 1