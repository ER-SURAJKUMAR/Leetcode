class Solution:
    def findMin(self, nums: list[int]) -> int:
        low, high = 0, len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            
            if nums[mid] > nums[high]:
                # The minimum must be in the right halves
                low = mid + 1
            elif nums[mid] < nums[high]:
                # The minimum is at mid or to the left of mid
                high = mid
            else:
                # When nums[mid] == nums[high], we cannot determine 
                # which side holds the minimum. Skip the duplicate.
                high -= 1
                
        return nums[low]