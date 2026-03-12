class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.components = n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.components -= 1
            return True
        return False

class Solution:
    def maxStability(self, n: int, edges: list[list[int]], k: int) -> int:
        
        def can_form(mid):
            dsu = DSU(n)
            edges_used = 0
            
            # 1. Mandatory Edges (must == 1)
            # They MUST be >= mid and cannot form a cycle.
            for u, v, s, must in edges:
                if must == 1:
                    if s < mid:
                        return False
                    if not dsu.union(u, v):
                        return False
                    edges_used += 1
            
            # 2. Optional Edges that satisfy mid WITHOUT upgrade
            for u, v, s, must in edges:
                if must == 0 and s >= mid:
                    if dsu.union(u, v):
                        edges_used += 1
            
            # 3. Optional Edges that satisfy mid WITH one upgrade
            upgrades_remaining = k
            for u, v, s, must in edges:
                if must == 0 and s < mid <= 2 * s:
                    if upgrades_remaining > 0:
                        if dsu.union(u, v):
                            upgrades_remaining -= 1
                            edges_used += 1
            
            # Spanning tree must have n-1 edges and 1 component
            return dsu.components == 1

        # Binary Search for the maximum possible minimum strength
        low, high = 1, 2 * 10**5
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if can_form(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans