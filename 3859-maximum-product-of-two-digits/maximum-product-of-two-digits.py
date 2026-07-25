class Solution:

    def maxProduct(self, n: int) -> int:
        # Extract digits as integers
        digits = sorted([int(d) for d in str(n)], reverse=True)

        # The maximum product comes from the two largest digits
        return digits[0] * digits[1]