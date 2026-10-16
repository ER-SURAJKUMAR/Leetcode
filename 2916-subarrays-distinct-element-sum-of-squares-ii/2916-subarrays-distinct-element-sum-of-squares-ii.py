class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Segment tree arrays
        # Tree size 4 * n
        tree_sum_sq = [0] * (4 * n)
        tree_sum = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def push(node, l, r):
            if lazy[node] != 0:
                v = lazy[node]
                mid = (l + r) // 2
                
                # Left child
                lc = 2 * node
                lazy[lc] = (lazy[lc] + v) % MOD
                len_l = (mid - l + 1)
                tree_sum_sq[lc] = (tree_sum_sq[lc] + 2 * v * tree_sum[lc] + v * v * len_l) % MOD
                tree_sum[lc] = (tree_sum[lc] + v * len_l) % MOD
                
                # Right child
                rc = 2 * node + 1
                lazy[rc] = (lazy[rc] + v) % MOD
                len_r = (r - mid)
                tree_sum_sq[rc] = (tree_sum_sq[rc] + 2 * v * tree_sum[rc] + v * v * len_r) % MOD
                tree_sum[rc] = (tree_sum[rc] + v * len_r) % MOD
                
                lazy[node] = 0

        def update(node, l, r, ql, qr, v):
            if ql > r or qr < l:
                return
            if ql <= l and r <= qr:
                lazy[node] = (lazy[node] + v) % MOD
                length = (r - l + 1)
                tree_sum_sq[node] = (tree_sum_sq[node] + 2 * v * tree_sum[node] + v * v * length) % MOD
                tree_sum[node] = (tree_sum[node] + v * length) % MOD
                return
            
            push(node, l, r)
            mid = (l + r) // 2
            update(2 * node, l, mid, ql, qr, v)
            update(2 * node + 1, mid + 1, r, ql, qr, v)
            
            tree_sum[node] = (tree_sum[2 * node] + tree_sum[2 * node + 1]) % MOD
            tree_sum_sq[node] = (tree_sum_sq[2 * node] + tree_sum_sq[2 * node + 1]) % MOD

        last_occ = {}
        total_sum_sq = 0
        current_sum_sq = 0
        
        for j in range(n):
            prev_idx = last_occ.get(nums[j], -1)
            last_occ[nums[j]] = j
            
            # Update range (prev_idx + 1, j) with +1
            update(1, 0, n - 1, prev_idx + 1, j, 1)
            
            # tree_sum_sq[1] now holds the sum of squares of distinct counts for all subarrays ending at index j
            total_sum_sq = (total_sum_sq + tree_sum_sq[1]) % MOD
            
        return total_sum_sq