class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Base case: S1 is "0"
        if n == 1:
            return "0"
        
        # The length of S_n is 2^n - 1. 
        # The middle element (the '1') is at index 2^(n-1).
        mid = 2**(n - 1)
        
        if k == mid:
            # The middle bit is always '1'
            return "1"
        elif k < mid:
            # The bit is in the first half, which is identical to S_{n-1}
            return self.findKthBit(n - 1, k)
        else:
            # The bit is in the second half. 
            # The second half is the inverted, reversed version of S_{n-1}.
            # The index relative to the reversed S_{n-1} is (2^n - k).
            res = self.findKthBit(n - 1, 2**n - k)
            
            # Return the inverted bit
            return "1" if res == "0" else "0"
            