class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        curr = n
        while True:
            temp = curr
            prod = 1
            while temp > 0:
                digit = temp % 10
                prod *= digit
                temp //= 10
            
            if prod % t == 0:
                return curr
            curr += 1