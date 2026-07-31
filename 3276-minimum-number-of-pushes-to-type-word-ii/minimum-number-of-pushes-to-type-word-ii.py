from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count frequency of each letter
        freq = Counter(word)
        
        # Sort frequencies in descending order
        sorted_freqs = sorted(freq.values(), reverse=True)
        
        total_pushes = 0
        
        # Calculate minimum pushes using greedy allocation
        for idx, count in enumerate(sorted_freqs):
            pushes_per_char = (idx // 8) + 1
            total_pushes += count * pushes_per_char
            
        return total_pushes