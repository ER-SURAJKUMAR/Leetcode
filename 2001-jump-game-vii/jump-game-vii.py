from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # If the destination itself is blocked, we can never reach it
        if s[-1] == '1':
            return False
        
        queue = deque([0])
        far_reached = 0
        n = len(s)
        
        while queue:
            curr = queue.popleft()
            
            # If we've reached the last index, return True
            if curr == n - 1:
                return True
            
            # Define the valid jumping window from the current position
            start = max(curr + minJump, far_reached + 1)
            end = min(curr + maxJump, n - 1)
            
            # Explore all unvisited valid indices in the window
            for j in range(start, end + 1):
                if s[j] == '0':
                    queue.append(j)
                    
            # Update the global boundary to avoid redundant checks in future iterations
            far_reached = max(far_reached, end)
            
        return False