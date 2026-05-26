class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # Create a set of all unique characters in the word
        unique_chars = set(word)
        
        special_count = 0
        
        # Iterate through the lowercase alphabet
        for i in range(26):
            lower_char = chr(ord('a') + i)
            upper_char = chr(ord('A') + i)
            
            # If both forms exist in our set, it's a special letter
            if lower_char in unique_chars and upper_char in unique_chars:
                special_count += 1
                
        return special_count