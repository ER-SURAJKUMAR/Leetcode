from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: list[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        
        # Map each value to all its corresponding indices
        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
            
        # BFS setup: queue stores (current_index, steps)
        queue = deque([(0, 0)])
        visited = {0}
        
        while queue:
            curr_idx, steps = queue.popleft()
            
            # If we reached the last index, return the steps taken
            if curr_idx == n - 1:
                return steps
                
            # Fetch all neighbors: i + 1, i - 1, and indices with the same value
            neighbors = [curr_idx + 1, curr_idx - 1] + graph[arr[curr_idx]]
            
            for neighbor in neighbors:
                if 0 <= neighbor < n and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
                    
            # CRITICAL OPTIMIZATION: Clear the list for this value to avoid 
            # redundant checks and prevent O(N^2) time complexity.
            graph[arr[curr_idx]] = []
            
        return 0