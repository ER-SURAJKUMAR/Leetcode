class Solution:
    def minElement(self, nums: list[int]) -> int:
        # Helper function to calculate the sum of digits of a number
        def get_digit_sum(n: int) -> int:
            digit_sum = 0
            while n > 0:
                digit_sum += n % 10
                n //= 10
            return digit_sum
        
        # Find the minimum digit sum across all numbers in the array
        return min(get_digit_sum(num) for num in nums)