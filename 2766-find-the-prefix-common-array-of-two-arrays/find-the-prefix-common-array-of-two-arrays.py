class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        n = len(A)
        C = [0] * n
        seen_count = {}
        common_count = 0
        
        for i in range(n):
            # Process element from array A
            num_a = A[i]
            seen_count[num_a] = seen_count.get(num_a, 0) + 1
            if seen_count[num_a] == 2:
                common_count += 1
                
            # Process element from array B
            num_b = B[i]
            seen_count[num_b] = seen_count.get(num_b, 0) + 1
            if seen_count[num_b] == 2:
                common_count += 1
                
            C[i] = common_count
            
        return C