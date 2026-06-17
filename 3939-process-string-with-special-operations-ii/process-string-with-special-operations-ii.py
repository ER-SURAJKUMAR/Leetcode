class Solution:
    def processStr(self, s: str, k: int) -> str:
        # Step 1: Forward pass to track lengths after each character operation
        lengths = []
        curr_len = 0
        
        for char in s:
            if char.isalpha():
                curr_len += 1
            elif char == '*':
                if curr_len > 0:
                    curr_len -= 1
            elif char == '#':
                curr_len *= 2
            elif char == '%':
                # Length does not change during a reverse
                pass
            lengths.append(curr_len)
            
        # If k is out of bounds of the final string length
        if k >= curr_len:
            return '.'
            
        # Step 2: Backward pass to trace the origin of index k
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            # Get the length *before* the current operation s[i]
            prev_len = lengths[i-1] if i > 0 else 0
            
            if char.isalpha():
                # If k points to the newly appended character
                if k == prev_len:
                    return char
                # Otherwise, k remains the same as it belongs to the prefix
            elif char == '*':
                # The removed character doesn't affect indices within the new length
                pass
            elif char == '#':
                # If k lies in the duplicated second half, map it back to the first half
                if k >= prev_len:
                    k -= prev_len
            elif char == '%':
                # Reverse mapping: k becomes the mirrored index
                k = prev_len - 1 - k
                
        return '.'