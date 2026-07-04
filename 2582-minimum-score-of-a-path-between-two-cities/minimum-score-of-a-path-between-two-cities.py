from collections import deque
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Build the adjacency list
        # graph[u] will store pairs of (v, distance)
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, dist in roads:
            graph[u].append((v, dist))
            graph[v].append((u, dist))
            
        # Step 2: BFS to traverse the connected component containing city 1
        min_score = float('inf')
        visited = set()
        queue = deque([1])
        visited.add(1)
        
        while queue:
            node = queue.popleft()
            
            for neighbor, dist in graph[node]:
                # Update the minimum score seen in this connected component
                if dist < min_score:
                    min_score = dist
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score