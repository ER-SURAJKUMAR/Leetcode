class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        i, j = 0, 0
        len1, len2 = len(nums1), len(nums2)
        
        # Traverse both arrays using two pointers
        while i < len1 and j < len2:
            if nums1[i] == nums2[j]:
                return nums1[i]  # Found the smallest common element
            elif nums1[i] < nums2[j]:
                i += 1  # Move the pointer in nums1 forward
            else:
                j += 1  # Move the pointer in nums2 forward
                
        return -1  # No common element found