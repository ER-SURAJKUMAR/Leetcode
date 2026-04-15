class Solution:
    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_distance = float('inf')
        found = False
        
        for i in range(n):
            if words[i] == target:
                found = True
                # Direct distance between indices
                abs_diff = abs(i - startIndex)
                
                # Minimum of going straight vs. wrapping around the circle
                current_distance = min(abs_diff, n - abs_diff)
                
                if current_distance < min_distance:
                    min_distance = current_distance
        
        return int(min_distance) if found else -1