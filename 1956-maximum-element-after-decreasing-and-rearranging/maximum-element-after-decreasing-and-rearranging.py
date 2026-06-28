class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        # Sort the array to match the smallest elements to the earliest positions
        arr.sort()
        
        # Track the current maximum valid value we can achieve
        current_max = 0
        
        for num in arr:
            # The next element can at most be 1 greater than the current_max
            if num > current_max:
                current_max += 1
                
        return current_max