import sys

# Increase recursion depth just in case
sys.setrecursionlimit(300000)

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        s_chars = list(s)
        
        # Binary Lifting for LCA
        LOGN = max(1, n.bit_length())
        up = [[0] * LOGN for _ in range(n)]
        tin = [0] * n
        tout = [0] * n
        timer = 0
        
        initial_mask = [0] * n
        parent = [-1] * n
        parent[0] = 0
        initial_mask[0] = 1 << (ord(s_chars[0]) - 97)
        
        # Iterative BFS/DFS to build tree ordering
        stack = [0]
        order = []
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    initial_mask[v] = initial_mask[u] ^ (1 << (ord(s_chars[v]) - 97))
                    stack.append(v)
                    
        # Compute Euler Tour in/out times and Binary Lifting table
        for u in order:
            up[u][0] = parent[u]
            for i in range(1, LOGN):
                up[u][i] = up[up[u][i - 1]][i - 1]

        st = [(0, -1)]
        children_idx = [0] * n
        while st:
            u, p = st[-1]
            if children_idx[u] == 0:
                timer += 1
                tin[u] = timer
            
            if children_idx[u] < len(adj[u]):
                v = adj[u][children_idx[u]]
                children_idx[u] += 1
                if v != p:
                    st.append((v, u))
            else:
                tout[u] = timer
                st.pop()

        def is_ancestor(u: int, v: int) -> bool:
            return tin[u] <= tin[v] and tout[u] >= tout[v]

        def get_lca(u: int, v: int) -> int:
            if is_ancestor(u, v):
                return u
            if is_ancestor(v, u):
                return v
            for i in range(LOGN - 1, -1, -1):
                if not is_ancestor(up[u][i], v):
                    u = up[u][i]
            return up[u][0]

        # Fenwick Tree for Range Update / Point Query
        bit = [0] * (n + 2)
        
        def bit_update(idx: int, val: int):
            while idx <= n + 1:
                bit[idx] ^= val
                idx += idx & (-idx)
                
        def bit_query(idx: int) -> int:
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res

        # Difference array initialization
        diff = [0] * (n + 2)
        for u in range(n):
            diff[tin[u]] ^= initial_mask[u]
            diff[tin[u] + 1] ^= initial_mask[u]
            
        for i in range(1, n + 1):
            bit[i] ^= diff[i]
            nxt = i + (i & (-i))
            if nxt <= n + 1:
                bit[nxt] ^= bit[i]

        ans = []
        
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new_c = parts[2]
                old_c = s_chars[u]
                if old_c != new_c:
                    s_chars[u] = new_c
                    change_mask = (1 << (ord(old_c) - 97)) ^ (1 << (ord(new_c) - 97))
                    # Apply change to entire subtree of u
                    bit_update(tin[u], change_mask)
                    bit_update(tout[u] + 1, change_mask)
            else:
                u = int(parts[1])
                v = int(parts[2])
                
                lca = get_lca(u, v)
                
                mask_u = bit_query(tin[u])
                mask_v = bit_query(tin[v])
                
                lca_char_mask = 1 << (ord(s_chars[lca]) - 97)
                path_mask = mask_u ^ mask_v ^ lca_char_mask
                
                ans.append((path_mask & (path_mask - 1)) == 0)

        return ans