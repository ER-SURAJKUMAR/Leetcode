class Solution:
    def isGood(self, nums: list[int]) -> bool:
        # The expected n is based on the length of base[n] = n + 1
        n = len(nums) - 1
        
        # Base case: base[n] requires n to be at least 1
        if n < 1:
            return False
        
        # Sort the array to easily compare with base[n]
        nums.sort()
        
        # Construct the target base[n] array
        # base[n] = [1, 2, ..., n-1, n, n]
        target = list(range(1, n + 1)) + [n]
        
        return nums == target