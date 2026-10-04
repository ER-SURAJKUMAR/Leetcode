class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0   # Min possible open brackets
        high = 0  # Max possible open brackets
        
        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            else:  # char == '*'
                low -= 1   # Treat '*' as ')'
                high += 1  # Treat '*' as '('
            
            # If high < 0, too many ')' encountered
            if high < 0:
                return False
            
            # low cannot be negative (we can't have negative required open brackets)
            if low < 0:
                low = 0
                
        return low == 0