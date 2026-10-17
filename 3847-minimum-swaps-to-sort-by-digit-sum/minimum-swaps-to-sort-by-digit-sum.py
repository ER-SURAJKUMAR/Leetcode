class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Helper function to compute the sum of digits of a number
        def digit_sum(x: int) -> int:
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s

        # Store elements along with their original index
        # (digit_sum, value, original_index)
        indexed_nums = []
        for i, val in enumerate(nums):
            indexed_nums.append((digit_sum(val), val, i))
        
        # Sort based on digit sum, then by value
        indexed_nums.sort(key=lambda item: (item[0], item[1]))
        
        # visited array to keep track of processed indices in cycle detection
        visited = [False] * n
        min_swaps = 0
        
        for i in range(n):
            # If the element is already visited or already in its correct position
            if visited[i] or indexed_nums[i][2] == i:
                continue
            
            # Count the size of the cycle
            cycle_size = 0
            curr = i
            
            while not visited[curr]:
                visited[curr] = True
                # Move to the original index of the element that belongs at 'curr'
                curr = indexed_nums[curr][2]
                cycle_size += 1
            
            # A cycle of length K requires K - 1 swaps
            if cycle_size > 0:
                min_swaps += (cycle_size - 1)
                
        return min_swaps