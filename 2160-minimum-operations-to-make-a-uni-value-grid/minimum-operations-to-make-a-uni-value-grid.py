class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        # Flatten the 2D grid into a 1D list
        nums = []
        for row in grid:
            nums.extend(row)
        
        # Sort the numbers to find the median
        nums.sort()
        
        n = len(nums)
        median = nums[n // 2]
        operations = 0
        
        # Reference remainder to check feasibility
        remainder = nums[0] % x
        
        for num in nums:
            # If the remainder is different, it's impossible to align them
            if num % x != remainder:
                return -1
            
            # Count operations needed to reach the median
            # Since we can only add/subtract x, the operations = |target - current| / x
            operations += abs(num - median) // x
            
        return operations