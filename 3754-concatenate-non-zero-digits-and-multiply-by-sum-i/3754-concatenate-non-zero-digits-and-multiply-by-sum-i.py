class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # Convert to string and filter out '0'
        non_zero_digits = [char for char in str(n) if char != '0']
        
        # If there are no non-zero digits, x = 0
        if not non_zero_digits:
            return 0
        
        # Form the integer x by joining the digits
        x = int("".join(non_zero_digits))
        
        # Calculate the sum of the non-zero digits
        digit_sum = sum(int(digit) for digit in non_zero_digits)
        
        # Return the product
        return x * digit_sum