class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        # Count how many patterns are present as a substring in the word
        return sum(1 for pattern in patterns if pattern in word)