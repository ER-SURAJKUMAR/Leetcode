class Solution:

    def checkDivisibility(self, n: int) -> bool:
        s = str(n)

        digit_sum = 0
        digit_prod = 1

        for char in s:
            digit = int(char)
            digit_sum += digit
            digit_prod *= digit

        total = digit_sum + digit_prod
        return n % total == 0