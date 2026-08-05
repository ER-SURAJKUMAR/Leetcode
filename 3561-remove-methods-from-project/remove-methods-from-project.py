from collections import deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        # Build graph adjacency list
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)
            
        # 1. Traversal to find all suspicious methods reachable from k
        suspicious = set([k])
        queue = deque([k])
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)
                    
        # 2. Check if any method outside the suspicious group invokes a method inside it
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                # Removal invalid: return all methods
                return list(range(n))
                
        # 3. Removal valid: return all non-suspicious methods
        return [i for i in range(n) if i not in suspicious]