class Solution:
    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        MOD = 10**9 + 7
        
        # Process each query sequentially
        for li, ri, ki, vi in queries:
            idx = li
            # Update elements in the specified range with the given step
            while idx <= ri:
                nums[idx] = (nums[idx] * vi) % MOD
                idx += ki
                
        # Calculate the bitwise XOR of all elements in the final array
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
            
        return xor_sum