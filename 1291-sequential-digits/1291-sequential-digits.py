class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        sample = "123456789"
        result = []
        
        # Get the digit lengths of our boundaries
        min_len = len(str(low))
        max_len = len(str(high))
        
        # Explore all possible lengths of sequential digits
        for length in range(min_len, max_len + 1):
            # Slide the window across the sample string
            for start in range(10 - length):
                substring = sample[start : start + length]
                num = int(substring)
                
                # Check if it falls within the requested range
                if low <= num <= high:
                    result.append(num)
                    
        return result