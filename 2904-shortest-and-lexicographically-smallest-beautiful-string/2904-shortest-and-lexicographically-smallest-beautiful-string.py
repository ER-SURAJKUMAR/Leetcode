class Solution:

    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        min_len = float("inf")
        ans = ""

        # Find all 1s indices
        ones = [i for i, ch in enumerate(s) if ch == "1"]

        # If total number of 1s is less than k, no beautiful substring exists
        if len(ones) < k:
            return ""

        # Any minimal beautiful substring must start at a '1' and end at a '1'
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]
            sub = s[start : end + 1]
            length = len(sub)

            if length < min_len:
                min_len = length
                ans = sub
            elif length == min_len:
                if sub < ans:
                    ans = sub

        return ans