from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        # Build the adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * n
        complete_components = 0
        
        for i in range(n):
            if not visited[i]:
                # Start a BFS/DFS to explore the current component
                component_vertices = []
                queue = [i]
                visited[i] = True
                
                while queue:
                    curr = queue.pop(0)
                    component_vertices.append(curr)
                    for neighbor in adj[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                
                # Count total vertices (V) in this component
                v_count = len(component_vertices)
                
                # Count total edges (E) inside this component by summing degrees
                edge_count_x2 = sum(len(adj[node]) for node in component_vertices)
                
                # For a complete graph, total edges must equal V * (V - 1) / 2
                # Or total degrees must equal V * (V - 1)
                if edge_count_x2 == v_count * (v_count - 1):
                    complete_components += 1
                    
        return complete_components