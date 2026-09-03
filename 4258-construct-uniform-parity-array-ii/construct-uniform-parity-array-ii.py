class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # Find the smallest element in the array
        min_val = min(nums1)
        
        # If the smallest element is odd, we can subtract it from any even number
        # to make that even number odd (Even - Odd = Odd). 
        # Thus, we can make all elements odd.
        if min_val % 2 != 0:
            return True
            
        # If the smallest element is even, we cannot make it odd because there is 
        # no smaller odd number to subtract from it.
        # We also cannot make the existing odd numbers even, because making an odd 
        # number even requires subtracting a smaller odd number (Odd - Odd = Even), 
        # which isn't possible since our absolute minimum is even.
        # Therefore, the only way it's possible is if all elements are ALREADY even.
        return all(x % 2 == 0 for x in nums1)