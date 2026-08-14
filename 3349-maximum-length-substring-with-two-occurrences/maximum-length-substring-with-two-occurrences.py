class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        counts = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            char = s[right]
            counts[char] = counts.get(char, 0) + 1
            
            # Shrink window until s[right] appears at most 2 times
            while counts[char] > 2:
                counts[s[left]] -= 1
                left += 1
            
            # Update maximum valid substring length
            max_len = max(max_len, right - left + 1)
            
        return max_len