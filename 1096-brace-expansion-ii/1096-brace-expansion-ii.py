class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        # Stack to hold tuple of (current_union_group, current_concatenation_group)
        # current_union_group: accumulated sets separated by ','
        # current_concatenation_group: accumulated sets concatenated together before a ','
        
        stack = []
        current_union = set()
        current_concat = {""}
        
        for char in expression:
            if char.isalpha():
                # Concatenate current letter with the current product
                current_concat = {s + char for s in current_concat}
                
            elif char == '{':
                # Save the current evaluation context to stack and start fresh
                stack.append((current_union, current_concat))
                current_union = set()
                current_concat = {""}
                
            elif char == '}':
                # Combine current concatenation into union
                current_union.update(current_concat)
                
                # Pop previous context from stack
                prev_union, prev_concat = stack.pop()
                
                # Perform Cartesian product of prev_concat with current_union
                current_concat = {
                    prefix + suffix
                    for prefix in prev_concat
                    for suffix in current_union
                }
                current_union = prev_union
                
            elif char == ',':
                # Add current concatenated group to the union, then reset concatenation
                current_union.update(current_concat)
                current_concat = {""}
                
        # Final union update
        current_union.update(current_concat)
        
        # Return unique words sorted lexicographically
        return sorted(list(current_union))