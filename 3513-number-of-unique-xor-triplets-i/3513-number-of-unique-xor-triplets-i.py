class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # For n >= 3, all numbers from 0 to (2^bit_length - 1) can be formed
        return 1 << n.bit_length()