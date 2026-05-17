from collections import deque

class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        queue = deque([start])
        
        while queue:
            curr = queue.popleft()
            
            # Check if we reached a 0 value
            if arr[curr] == 0:
                return True
            
            # Skip if already visited
            if arr[curr] < 0:
                continue
                
            jump = arr[curr]
            # Mark as visited by making it negative
            arr[curr] = -arr[curr]
            
            # Explore valid moves
            for next_idx in (curr + jump, curr - jump):
                if 0 <= next_idx < len(arr) and arr[next_idx] >= 0:
                    queue.append(next_idx)
                    
        return False