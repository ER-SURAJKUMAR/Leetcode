class Solution:
    def maxStability(self, n: int, edges: list[list[int]], k: int) -> int:
        
        def can_achieve(min_val):
            # Reset DSU state for every binary search check
            parent = list(range(n))
            components = n
            
            def find(i):
                if parent[i] == i: return i
                parent[i] = find(parent[i])
                return parent[i]

            def union(i, j):
                nonlocal components
                root_i, root_j = find(i), find(j)
                if root_i != root_j:
                    parent[root_i] = root_j
                    components -= 1
                    return True
                return False

            # 1. Mandatory Edges: Must be >= min_val and not form cycles
            for u, v, s, must in edges:
                if must == 1:
                    if s < min_val: return False
                    if not union(u, v): return False
            
            # 2. Strong Optional: Can reach min_val without upgrade
            for u, v, s, must in edges:
                if must == 0 and s >= min_val:
                    union(u, v)
            
            # 3. Weak Optional: Need upgrade to reach min_val
            upgrades = k
            for u, v, s, must in edges:
                if must == 0 and s < min_val <= 2 * s:
                    if upgrades > 0:
                        if union(u, v):
                            upgrades -= 1
            
            return components == 1

        # Binary Search Range: 1 to max possible upgraded strength
        low, high = 1, 200000
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if can_achieve(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans