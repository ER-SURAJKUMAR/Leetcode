class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Step 1: Find the last occurrence index of each character
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        stack = []
        # Keep track of characters already present in the stack
        seen = set()
        
        for i, char in enumerate(s):
            # If the character is already in our result, skip it
            if char in seen:
                continue
            
            # Maintain the monotonic increasing order (lexicographically smallest)
            # Pop the top element if:
            # 1. The stack is not empty
            # 2. The top character is lexicographically larger than the current character
            # 3. The top character appears again later in the string
            while stack and stack[-1] > char and last_occurrence[stack[-1]] > i:
                removed_char = stack.pop()
                seen.remove(removed_char)
                
            # Push the current character to the stack and mark it as seen
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)