class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        prefixes = set()
        
        # Step 1: Populate the set with all possible prefixes from arr1
        for num in arr1:
            while num > 0:
                prefixes.add(num)
                num //= 10  # Remove the last digit to get the next prefix
        
        max_length = 0
        
        # Step 2: Check prefixes of numbers in arr2 against the set
        for num in arr2:
            while num > 0:
                if num in prefixes:
                    # If found, calculate the length of this prefix
                    # Converting to string gives the number of digits
                    max_length = max(max_length, len(str(num)))
                    break  # Break early since shorter prefixes of this number won't exceed this length
                num //= 10
                
        return max_length