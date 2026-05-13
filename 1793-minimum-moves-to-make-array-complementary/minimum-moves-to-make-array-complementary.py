from collections import defaultdict

class Solution:
    def minMoves(self, nums: list[int], limit: int) -> int:
        # diff[i] will store the change in moves needed if the target sum is i
        # The range of possible sums is [2, 2 * limit]
        diff = [0] * (2 * limit + 2)
        n = len(nums)
        
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            
            # Identify the boundaries for 1-move range
            # min_val + 1 is the smallest sum reachable with 1 replacement
            # max_val + limit is the largest sum reachable with 1 replacement
            min_val = min(a, b)
            max_val = max(a, b)
            
            # 1. Default: 2 moves for every pair to reach any sum
            diff[2] += 2
            diff[2 * limit + 1] -= 2
            
            # 2. Improvement: To reach the range [min_val + 1, max_val + limit], 
            # we only need 1 move instead of 2.
            diff[min_val + 1] -= 1
            diff[max_val + limit + 1] += 1
            
            # 3. Improvement: To reach exactly a + b, 
            # we need 0 moves instead of 1.
            diff[a + b] -= 1
            diff[a + b + 1] += 1
            
        # Sweep through the difference array to find the minimum moves
        min_moves = n # Maximum possible moves is n
        current_moves = 0
        for i in range(2, 2 * limit + 1):
            current_moves += diff[i]
            if current_moves < min_moves:
                min_moves = current_moves
                
        return min_moves