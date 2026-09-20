class Solution:
    def reverseDegree(self, s: str) -> int:
        total_degree = 0
        
        for i, ch in enumerate(s, 1):
            # 'a' -> 26, 'b' -> 25, ..., 'z' -> 1
            reversed_val = 26 - (ord(ch) - ord('a'))
            total_degree += reversed_val * i
            
        return total_degree