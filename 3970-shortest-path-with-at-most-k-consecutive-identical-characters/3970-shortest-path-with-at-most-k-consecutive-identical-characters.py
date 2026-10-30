import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        # Build adjacency list: u -> list of (v, weight)
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            
        # dist[u][c] stores the minimum distance to reach node `u` 
        # with `c` consecutive occurrences of character labels[u].
        # Initialize with infinity.
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        
        # Priority queue stores tuples of: (current_distance, current_node, consecutive_count)
        # Starting at node 0 with consecutive count = 1 for labels[0]
        pq = [(0, 0, 1)]
        dist[0][1] = 0
        
        while pq:
            d, u, count = heapq.heappop(pq)
            
            # If we reached the target node n - 1, return the distance
            if u == n - 1:
                return d
            
            # If we found a shorter path to (u, count) already, skip
            if d > dist[u][count]:
                continue
            
            curr_char = labels[u]
            
            for v, w in adj[u]:
                next_char = labels[v]
                
                if next_char == curr_char:
                    next_count = count + 1
                else:
                    next_count = 1
                
                # Check if the consecutive character constraint is respected
                if next_count <= k:
                    if d + w < dist[v][next_count]:
                        dist[v][next_count] = d + w
                        heapq.heappush(pq, (d + w, v, next_count))
                        
        return -1