class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Step 1: Count trailing zeros for each row
        trailing_zeros = []
        for row in grid:
            count = 0
            for i in range(n - 1, -1, -1):
                if row[i] == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)
        
        res = 0
        # Step 2: Greedy swap to satisfy requirements
        for i in range(n):
            # Target: row i needs at least (n - 1 - i) trailing zeros
            target = n - 1 - i
            
            # Find the nearest row that satisfies the requirement
            found_idx = -1
            for j in range(i, n):
                if trailing_zeros[j] >= target:
                    found_idx = j
                    break
            
            # If no row satisfies the condition, return -1
            if found_idx == -1:
                return -1
            
            # Move the row from found_idx to i using adjacent swaps
            # This is essentially one pass of bubble sort logic
            res += (found_idx - i)
            
            # Update the list to reflect the new positions
            row_to_move = trailing_zeros.pop(found_idx)
            trailing_zeros.insert(i, row_to_move)
            
        return res