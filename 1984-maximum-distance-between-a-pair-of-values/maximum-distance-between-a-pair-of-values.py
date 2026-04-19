class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        i = 0
        j = 0
        max_dist = 0
        n1, n2 = len(nums1), len(nums2)
        
        # Use two pointers to find the maximum j - i
        while i < n1 and j < n2:
            # Check if the current pair is valid
            if nums1[i] <= nums2[j]:
                # Update max distance
                max_dist = max(max_dist, j - i)
                # Try to increase distance by moving j
                j += 1
            else:
                # If nums1[i] > nums2[j], we need a smaller nums1[i]
                # Increment i to potentially satisfy the condition
                i += 1
                # Optimization: j should always be at least equal to i
                if j < i:
                    j = i
                    
        return max_dist