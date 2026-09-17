class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        inf = float('inf')
        
        # min_len[i] stores the min length of sub-array with sum == target in arr[0...i]
        min_len = [inf] * n
        
        left = 0
        current_sum = 0
        min_total_len = inf
        best_so_far = inf
        
        for right in range(n):
            current_sum += arr[right]
            
            # Shrink the window while current_sum is greater than target
            while current_sum > target:
                current_sum -= arr[left]
                left += 1
            
            # If a valid sub-array is found ending at 'right'
            if current_sum == target:
                curr_len = right - left + 1
                
                # Check if there is a non-overlapping valid sub-array to the left
                if left > 0 and min_len[left - 1] != inf:
                    min_total_len = min(min_total_len, curr_len + min_len[left - 1])
                
                best_so_far = min(best_so_far, curr_len)
            
            min_len[right] = best_so_far
            
        return min_total_len if min_total_len != inf else -1