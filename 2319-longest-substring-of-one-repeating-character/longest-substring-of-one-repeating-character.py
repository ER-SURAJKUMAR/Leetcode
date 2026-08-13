class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        n = len(s)
        s_list = list(s)
        
        # Arrays to represent segment tree nodes
        tree_max = [0] * (4 * n)
        tree_pref_len = [0] * (4 * n)
        tree_suff_len = [0] * (4 * n)
        tree_pref_char = [''] * (4 * n)
        tree_suff_char = [''] * (4 * n)
        
        def merge(node: int, l_len: int, r_len: int):
            left = 2 * node
            right = 2 * node + 1
            
            tree_pref_char[node] = tree_pref_char[left]
            tree_suff_char[node] = tree_suff_char[right]
            
            # Combine max length
            tree_max[node] = max(tree_max[left], tree_max[right])
            if tree_suff_char[left] == tree_pref_char[right]:
                tree_max[node] = max(tree_max[node], tree_suff_len[left] + tree_pref_len[right])
            
            # Combine prefix length
            tree_pref_len[node] = tree_pref_len[left]
            if tree_pref_len[left] == l_len and tree_pref_char[left] == tree_pref_char[right]:
                tree_pref_len[node] = l_len + tree_pref_len[right]
                
            # Combine suffix length
            tree_suff_len[node] = tree_suff_len[right]
            if tree_suff_len[right] == r_len and tree_suff_char[right] == tree_suff_char[left]:
                tree_suff_len[node] = r_len + tree_suff_len[left]

        def build(node: int, start: int, end: int):
            if start == end:
                char = s_list[start]
                tree_max[node] = 1
                tree_pref_len[node] = 1
                tree_suff_len[node] = 1
                tree_pref_char[node] = char
                tree_suff_char[node] = char
                return
            
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            merge(node, mid - start + 1, end - mid)

        def update(node: int, start: int, end: int, idx: int, char: str):
            if start == end:
                s_list[idx] = char
                tree_pref_char[node] = char
                tree_suff_char[node] = char
                return
            
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node, start, mid, idx, char)
            else:
                update(2 * node + 1, mid + 1, end, idx, char)
                
            merge(node, mid - start + 1, end - mid)

        # Build initial Segment Tree
        build(1, 0, n - 1)
        
        result = []
        for char, idx in zip(queryCharacters, queryIndices):
            if s_list[idx] != char:
                update(1, 0, n - 1, idx, char)
            result.append(tree_max[1])
            
        return result