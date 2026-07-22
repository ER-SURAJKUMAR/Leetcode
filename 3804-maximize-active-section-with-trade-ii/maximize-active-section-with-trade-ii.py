class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        total_ones = s.count('1')
        
        # 1. Extract zero groups and map each character index to its zero group
        zero_groups = []       # list of [start_idx, length]
        zero_group_idx = [-1] * n
        
        curr_group_idx = -1
        for i, char in enumerate(s):
            if char == '0':
                if i > 0 and s[i - 1] == '0':
                    zero_groups[-1][1] += 1
                else:
                    zero_groups.append([i, 1])
                    curr_group_idx += 1
            zero_group_idx[i] = curr_group_idx

        num_zero_groups = len(zero_groups)
        if num_zero_groups < 2:
            return [total_ones] * len(queries)

        # 2. Build Sparse Table for adjacent zero-group length sums
        sum_adj = [zero_groups[i][1] + zero_groups[i + 1][1] for i in range(num_zero_groups - 1)]

        m = len(sum_adj)
        log_m = m.bit_length()
        st = [[0] * m for _ in range(log_m)]
        st[0] = list(sum_adj)
        
        for i in range(1, log_m):
            len_prev = 1 << (i - 1)
            for j in range(m - (1 << i) + 1):
                st[i][j] = max(st[i - 1][j], st[i - 1][j + len_prev])

        def query_st(l_idx, r_idx):
            if l_idx > r_idx:
                return 0
            k = (r_idx - l_idx + 1).bit_length() - 1
            return max(st[k][l_idx], st[k][r_idx - (1 << k) + 1])

        # 3. Process each query
        ans = []
        for l, r in queries:
            g_l = zero_group_idx[l]
            g_r = zero_group_idx[r]

            left_len = 0
            if s[l] == '0':
                left_len = zero_groups[g_l][0] + zero_groups[g_l][1] - l

            right_len = 0
            if s[r] == '0':
                right_len = r - zero_groups[g_r][0] + 1

            best_active = total_ones

            # Case 1: s[l] and s[r] belong to adjacent zero-groups
            if s[l] == '0' and s[r] == '0' and g_l + 1 == g_r:
                best_active = max(best_active, total_ones + left_len + right_len)

            # Case 2: Internal adjacent full zero-groups completely inside [l, r]
            start_adj_idx = g_l + 1 if s[l] == '0' else g_l + 1
            end_adj_idx = g_r - 1 if s[r] == '0' else g_r
            if start_adj_idx <= end_adj_idx - 1:
                best_active = max(best_active, total_ones + query_st(start_adj_idx, end_adj_idx - 1))

            # Case 3: Clipped left zero-group + next full zero-group
            if s[l] == '0' and g_l + 1 <= (g_r - 1 if s[r] == '0' else g_r):
                best_active = max(best_active, total_ones + left_len + zero_groups[g_l + 1][1])

            # Case 4: Clipped right zero-group + previous full zero-group
            if s[r] == '0' and g_l < g_r - 1:
                best_active = max(best_active, total_ones + right_len + zero_groups[g_r - 1][1])

            ans.append(best_active)

        return ans