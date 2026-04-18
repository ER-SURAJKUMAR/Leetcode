class Solution:
    def mirrorDistance(self, n: int) -> int:
        # Convert integer to string and reverse it
        # int() handles leading zeros (e.g., "01" becomes 1)
        reversed_n = int(str(n)[::-1])
        
        # Calculate the absolute difference
        return abs(n - reversed_n)