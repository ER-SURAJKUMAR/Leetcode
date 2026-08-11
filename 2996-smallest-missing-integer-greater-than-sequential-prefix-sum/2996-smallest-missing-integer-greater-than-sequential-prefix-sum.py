class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        # Step 1: Find the sum of the longest sequential prefix
        prefix_sum = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            prefix_sum += nums[i]
            i += 1
            
        # Step 2: Convert to set for O(1) lookups and find smallest missing integer >= prefix_sum
        num_set = set(nums)
        x = prefix_sum
        while x in num_set:
            x += 1
            
        return x