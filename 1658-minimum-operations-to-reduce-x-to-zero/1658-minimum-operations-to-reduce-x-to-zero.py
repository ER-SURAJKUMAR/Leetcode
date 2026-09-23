class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        
        if target == 0:
            return len(nums)
        if target < 0:
            return -1
        
        left = 0
        current_sum = 0
        max_len = -1
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Shrink window from the left until current_sum <= target
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
            
            # Record maximum length of sub-array matching target sum
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
                
        return len(nums) - max_len if max_len != -1 else -1