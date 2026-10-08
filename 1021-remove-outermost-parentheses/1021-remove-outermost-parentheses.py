class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        opened = 0
        
        for char in s:
            if char == '(':
                # If depth > 0, this '(' is not the outermost parenthesis of a primitive string
                if opened > 0:
                    res.append(char)
                opened += 1
            else:
                opened -= 1
                # If depth > 0 after decrementing, this ')' is not the outermost parenthesis
                if opened > 0:
                    res.append(char)
                    
        return "".join(res)