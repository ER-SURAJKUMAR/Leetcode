class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Step 1: Record first and last occurrences of each character
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        valid_intervals = []

        # Step 2: Expand intervals for each character's initial starting position
        for ch in first:
            L = first[ch]
            R = last[ch]
            is_valid = True
            
            i = L
            while i <= R:
                c = s[i]
                if first[c] < L:
                    # If an internal character starts before L, this L cannot be a valid start
                    is_valid = False
                    break
                R = max(R, last[c])
                i += 1
            
            if is_valid:
                valid_intervals.append((L, R))

        # Step 3: Sort valid intervals by their end index (R) ascending
        valid_intervals.sort(key=lambda x: x[1])

        # Step 4: Greedy selection of non-overlapping intervals
        result = []
        prev_end = -1
        for L, R in valid_intervals:
            if L > prev_end:
                result.append(s[L:R + 1])
                prev_end = R

        return result