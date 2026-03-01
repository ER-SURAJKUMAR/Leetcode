class Solution:
    def minPartitions(self, n: str) -> int:
        # The answer is simply the largest digit in the string.
        # Since 'n' is a string, we can use the max() function 
        # and convert the resulting character to an integer.
        return int(max(n))