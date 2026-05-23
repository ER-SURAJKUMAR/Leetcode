class Solution:
    def check(self, nums: list[int]) -> bool:
        count_drops = 0
        n = len(nums)
        
        for i in range(n):
            # Use modulo to smoothly check the transition from the last element back to the first
            if nums[i] > nums[(i + 1) % n]:
                count_drops += 1
                
            # If we find more than one drop, it cannot be a sorted rotated array
            if count_drops > 1:
                return False
                
        return True