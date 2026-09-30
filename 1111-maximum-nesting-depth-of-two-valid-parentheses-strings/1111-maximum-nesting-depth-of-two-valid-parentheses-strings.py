class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        depth = 0
        
        for char in seq:
            if char == '(':
                # Assign to A (0) or B (1) based on current depth
                ans.append(depth % 2)
                depth += 1
            else:
                # Decrement first to match the depth of its opening parenthesis
                depth -= 1
                ans.append(depth % 2)
                
        return ans