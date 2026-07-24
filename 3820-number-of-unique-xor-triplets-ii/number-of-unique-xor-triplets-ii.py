class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        # Collect unique values from nums
        U = list(set(nums))
        m = len(U)
        
        # Base set initialized with unique elements (covers i = j = k or i = j != k cases)
        unique_xors = set(U)
        
        # Step 1: Find all unique pair XORs
        P = set()
        for i in range(m):
            for j in range(i + 1, m):
                P.add(U[i] ^ U[j])
                
        # Step 2: Combine pair XORs with single elements from U
        for p in P:
            for z in U:
                unique_xors.add(p ^ z)
                
        return len(unique_xors)