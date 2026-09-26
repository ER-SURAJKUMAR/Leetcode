from typing import List

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        # Convert the knowledge array into a dictionary for O(1) lookups
        knowledge_dict = {k: v for k, v in knowledge}
        
        result = []
        current_key = []
        in_bracket = False
        
        for char in s:
            if char == '(':
                # We are entering a bracket, start recording the key
                in_bracket = True
            elif char == ')':
                # Bracket closed, look up the key
                key = "".join(current_key)
                result.append(knowledge_dict.get(key, "?"))
                # Reset for the next potential key
                current_key = []
                in_bracket = False
            elif in_bracket:
                # Build the key character by character
                current_key.append(char)
            else:
                # Normal character outside of brackets
                result.append(char)
                
        return "".join(result)