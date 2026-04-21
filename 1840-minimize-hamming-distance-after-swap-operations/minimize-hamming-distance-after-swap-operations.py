from collections import defaultdict

class Solution:
    def minimumHammingDistance(self, source: list[int], target: list[int], allowedSwaps: list[list[int]]) -> int:
        n = len(source)
        parent = list(range(n))
        
        # Helper function for Union-Find (Path Compression)
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        # Helper function for Union-Find (Union)
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j

        # 1. Group indices into connected components
        for a, b in allowedSwaps:
            union(a, b)
            
        # 2. Map root representative to the list of indices in that component
        components = defaultdict(list)
        for i in range(n):
            components[find(i)].append(i)
            
        total_matches = 0
        
        # 3. For each component, find how many source elements match target requirements
        for root in components:
            indices = components[root]
            
            # Count elements available in 'source' for this component
            source_counts = defaultdict(int)
            for idx in indices:
                source_counts[source[idx]] += 1
                
            # See how many 'target' elements at these indices can be satisfied
            for idx in indices:
                val = target[idx]
                if source_counts[val] > 0:
                    total_matches += 1
                    source_counts[val] -= 1
                    
        # Hamming distance is the total elements minus those we successfully matched
        return n - total_matches