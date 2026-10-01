class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Map closing brackets to their corresponding opening brackets
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:
                # Pop the topmost element if stack is not empty, else use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the mapped opening bracket doesn't match the top element, it's invalid
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, so push it onto the stack
                stack.append(char)
                
        # If the stack is empty, all brackets were matched correctly
        return not stack