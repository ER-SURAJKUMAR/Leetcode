class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # We can always construct an array with uniform parity (all even or all odd):
        # 1. To make all elements EVEN:
        #    - If all elements in nums1 are even, keep them as is.
        #    - If there is at least one odd element, subtract an odd element from every odd element
        #      to turn them into even (odd - odd = even), while keeping even elements as is.
        # 2. To make all elements ODD:
        #    - If there is at least one odd element, keep all odd elements as is, and subtract an
        #      odd element from every even element (even - odd = odd).
        #    - If all elements in nums1 are even, we can subtract any non-equal even element from
        #      another to get an even result, but we cannot create an odd number without an odd input.
        #      However, making all elements EVEN is already guaranteed for any valid distinct array.
        return True