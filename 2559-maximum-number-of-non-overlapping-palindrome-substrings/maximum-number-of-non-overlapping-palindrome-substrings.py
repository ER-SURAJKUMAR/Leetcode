class Solution:

    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        count = 0
        i = 0

        while i < n:
            # We only need to check for palindromes of length k and k + 1.
            # Any palindrome of length > k + 1 contains a smaller palindrome
            # of length k or k + 1 inside it.
            found = False
            for length in (k, k + 1):
                # Try every possible center for a palindrome of this length
                # that ends at or before index `right`
                right = i + length - 1
                if right < n:
                    # Check if s[i : right + 1] is a palindrome
                    sub = s[i : right + 1]
                    if sub == sub[::-1]:
                        count += 1
                        i = right + 1  # Greedy choice: move past the found palindrome
                        found = True
                        break

            if not found:
                i += 1

        return count