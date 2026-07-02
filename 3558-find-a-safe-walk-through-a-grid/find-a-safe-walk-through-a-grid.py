import heapq

class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Directions for moving up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # min_cost[r][c] will store the minimum health damage taken to reach (r, c)
        min_cost = [[float('inf')] * n for _ in range(m)]
        min_cost[0][0] = grid[0][0]
        
        # Min-heap stores tuples: (current_cost, row, col)
        pq = [(grid[0][0], 0, 0)]
        
        while pq:
            cost, r, c = heapq.heappop(pq)
            
            # If we reached the bottom-right corner
            if r == m - 1 and c == n - 1:
                return (health - cost) >= 1
            
            # Skip if we found a better path to this cell already
            if cost > min_cost[r][c]:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check grid boundaries
                if 0 <= nr < m and 0 <= nc < n:
                    next_cost = cost + grid[nr][nc]
                    
                    # If this path to (nr, nc) is cheaper, update and push to heap
                    if next_cost < min_cost[nr][nc]:
                        min_cost[nr][nc] = next_cost
                        heapq.heappush(pq, (next_cost, nr, nc))
                        
        return False