from collections import Counter


class Solution:

    def smallestPalindrome(self, s: str) -> str:
        counts = Counter(s)

        left_half = []
        mid_char = ""

        # Sort characters to ensure lexicographical order
        for char in sorted(counts.keys()):
            count = counts[char]

            # If odd count, set as middle character
            if count % 2 == 1:
                mid_char = char

            # Add half of the count to the left half
            left_half.append(char * (count // 2))

        left_str = "".join(left_half)

        # Combine left half, middle character, and mirrored right half
        return left_str + mid_char + left_str[::-1]