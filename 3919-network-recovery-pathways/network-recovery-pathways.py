from collections import deque

class Solution:
    def findMaxPathScore(self, edges: list[list[int]], online: list[bool], k: int) -> int:
        # Determine the number of nodes from the length of the online list
        n = len(online)
        
        # Step 1: Filter out edges that involve offline intermediate nodes.
        valid_edges = []
        max_edge_cost = -1
        
        for u, v, cost in edges:
            if online[u] and online[v]:
                valid_edges.append((u, v, cost))
                if cost > max_edge_cost:
                    max_edge_cost = cost
                    
        if not valid_edges:
            return -1

        # Step 2: Compute in-degrees for topological sort using valid edges
        adj_full = [[] for _ in range(n)]
        in_degree_full = [0] * n
        for u, v, cost in valid_edges:
            adj_full[u].append((v, cost))
            in_degree_full[v] += 1
            
        topo_order = []
        queue = deque([i for i in range(n) if in_degree_full[i] == 0])
        
        while queue:
            u = queue.popleft()
            topo_order.append(u)
            for v, _ in adj_full[u]:
                in_degree_full[v] -= 1
                if in_degree_full[v] == 0:
                    queue.append(v)

        # Step 3: Helper function to check if a valid path exists with all edge costs >= mid
        def can_reach_with_score(mid_score: int) -> bool:
            dp = [float('inf')] * n
            dp[0] = 0
            
            for u in topo_order:
                if dp[u] == float('inf'):
                    continue
                for v, cost in adj_full[u]:
                    if cost >= mid_score:
                        if dp[u] + cost < dp[v]:
                            dp[v] = dp[u] + cost
                            
            return dp[n - 1] <= k

        # Step 4: Binary search on the answer
        low = 0
        high = max_edge_cost
        ans = -1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if can_reach_with_score(mid):
                ans = mid  
                low = mid + 1
            else:
                high = mid - 1
                
        return ans