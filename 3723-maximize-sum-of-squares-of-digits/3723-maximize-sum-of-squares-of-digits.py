class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # Check if the sum is out of the valid range
        if sum < 1 or sum > 9 * num:
            return ""
        
        n_nines = sum // 9
        remainder = sum % 9
        
        if remainder > 0:
            n_zeros = num - n_nines - 1
            digits = ['9'] * n_nines + [str(remainder)] + ['0'] * n_zeros
        else:
            n_zeros = num - n_nines
            digits = ['9'] * n_nines + ['0'] * n_zeros
            
        return "".join(digits)