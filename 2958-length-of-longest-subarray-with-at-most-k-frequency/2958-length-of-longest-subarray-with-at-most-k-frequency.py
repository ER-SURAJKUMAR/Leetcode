from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        max_length = 0
        
        for right in range(len(nums)):
            freq[nums[right]] += 1
            
            # Shrink window until the frequency constraint is satisfied
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1
                
            max_length = max(max_length, right - left + 1)
            
        return max_length