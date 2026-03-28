class Solution:
    def findTheString(self, lcp: list[list[int]]) -> str:
        n = len(lcp)
        parent = list(range(n))
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union( i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j

        # Step 1: Group characters that must be equal
        for i in range(n):
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    union(i, j)
        
        # Step 2: Assign letters greedily
        res = [None] * n
        curr_char_idx = 0
        groups = {}
        
        for i in range(n):
            root = find(i)
            if root not in groups:
                if curr_char_idx >= 26:
                    return ""
                groups[root] = chr(ord('a') + curr_char_idx)
                curr_char_idx += 1
            res[i] = groups[root]
            
        word = "".join(res)
        
        # Step 3: Verify the matrix
        # We check from back to front to use DP-style verification
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                expected = 0
                if word[i] == word[j]:
                    expected = 1
                    if i + 1 < n and j + 1 < n:
                        expected += lcp[i+1][j+1]
                
                if lcp[i][j] != expected:
                    return ""
                    
        return word