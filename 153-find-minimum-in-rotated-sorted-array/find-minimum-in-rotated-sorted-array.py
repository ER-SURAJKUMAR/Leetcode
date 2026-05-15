class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        
        # If the array is not rotated at all (or rotated n times)
        # the first element is the smallest.
        if nums[left] <= nums[right]:
            return nums[left]
        
        while left <= right:
            mid = (left + right) // 2
            
            # Check if mid+1 is the minimum element
            # Example: [4, 5, 6, 7, 0, 1, 2] -> 7 > 0, so 0 is min
            if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            # Check if mid itself is the minimum element
            # Example: [4, 5, 6, 7, 0, 1, 2] -> 7 > 0, mid is 7, mid+1 is 0
            if mid - 1 >= 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            # If the middle element is greater than the first element,
            # the pivot (minimum) must be in the right half.
            if nums[mid] > nums[0]:
                left = mid + 1
            # If nums[mid] is smaller than the first element,
            # the pivot is in the left half.
            else:
                right = mid - 1
                
        return nums[0]