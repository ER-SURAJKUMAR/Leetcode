class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        """
        To solve this efficiently in O(n), we derive a relationship between F(k) and F(k-1).
        
        Let S be the sum of all elements in nums.
        F(0) = 0*nums[0] + 1*nums[1] + ... + (n-1)*nums[n-1]
        F(1) = 0*nums[n-1] + 1*nums[0] + 2*nums[1] + ... + (n-1)*nums[n-2]
        
        Difference:
        F(1) - F(0) = nums[0] + nums[1] + ... + nums[n-2] - (n-1)*nums[n-1]
        F(1) - F(0) = (S - nums[n-1]) - (n-1)*nums[n-1]
        F(1) - F(0) = S - n * nums[n-1]
        
        General formula:
        F(k) = F(k-1) + S - n * nums[n-k]
        """
        n = len(nums)
        s = sum(nums)
        
        # Calculate F(0)
        current_f = sum(i * val for i, val in enumerate(nums))
        max_f = current_f
        
        # Iteratively calculate F(1) to F(n-1) using the derived formula
        for k in range(1, n):
            # nums[n-k] gives the element that moves from the last position to the first
            current_f = current_f + s - n * nums[n - k]
            if current_f > max_f:
                max_f = current_f
                
        return max_f