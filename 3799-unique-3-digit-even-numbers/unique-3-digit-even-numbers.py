from collections import Counter

class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        digit_counts = Counter(digits)
        valid_count = 0
        
        # Check all 3-digit even numbers (100 to 998)
        for num in range(100, 1000, 2):
            d1, d2, d3 = num // 100, (num // 10) % 10, num % 10
            num_counts = Counter([d1, d2, d3])
            
            # Verify if the input array has enough copies of each required digit
            if all(digit_counts[d] >= count for d, count in num_counts.items()):
                valid_count += 1
                
        return valid_count