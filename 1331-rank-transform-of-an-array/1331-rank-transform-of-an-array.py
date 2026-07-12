class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        # Step 1: Get sorted unique elements
        unique_sorted = sorted(set(arr))
        
        # Step 2: Create a mapping from element to its rank
        rank_map = {num: rank for rank, num in enumerate(unique_sorted, 1)}
        
        # Step 3: Replace each element in the original array with its rank
        return [rank_map[num] for num in arr]