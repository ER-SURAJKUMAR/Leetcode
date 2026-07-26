class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        # Track 3 largest and 2 smallest numbers in O(N) time
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')

        for num in nums:
            # Update maximums
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num

            # Update minimums
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

        return max(max1 * max2 * max3, min1 * min2 * max1)