class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed = 0
        close_needed = 0
        
        for char in s:
            if char == '(':
                # We have an unmatched opening parenthesis, so we need a closing one
                close_needed += 1
            else:
                # We encountered a closing parenthesis
                if close_needed > 0:
                    # It matches with an existing unmatched opening parenthesis
                    close_needed -= 1
                else:
                    # No unmatched opening parenthesis exists, so we must add one
                    open_needed += 1
                    
        # Total additions is the sum of unmatched open and close parentheses
        return open_needed + close_needed