from collections import Counter

class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        count = Counter(nums)
        max_len = 1
        
        # Handle the special case for 1
        if 1 in count:
            c1 = count[1]
            if c1 % 2 == 0:
                max_len = max(max_len, c1 - 1)
            else:
                max_len = max(max_len, c1)
        
        # Process numbers > 1
        for num in count:
            if num == 1:
                continue
                
            current_len = 0
            x = num
            
            # Keep climbing if we have at least 2 instances of 'x' 
            # and the next square exists in our frequency map
            while x in count and count[x] >= 2 and (x * x) in count:
                current_len += 2
                x = x * x
            
            # The current 'x' becomes the peak element of this chain
            # (We only need at least 1 instance of the peak element)
            if x in count and count[x] >= 1:
                current_len += 1
            else:
                # If we broke out because x wasn't available at all,
                # the previous element should have been treated as a peak.
                current_len -= 1
                
            max_len = max(max_len, current_len)
            
        return max_len