class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        result = []
        
        for word in words:
            # Calculate the total weight of the current word
            total_weight = sum(weights[ord(char) - ord('a')] for char in word)
            
            # Find the remainder when divided by 26
            remainder = total_weight % 26
            
            # Map the remainder to reverse alphabetical order (0 -> 'z', 1 -> 'y', ..., 25 -> 'a')
            mapped_char = chr(ord('z') - remainder)
            
            result.append(mapped_char)
            
        return "".join(result)