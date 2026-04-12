class Solution:
    def minimumDistance(self, word: str) -> int:
        def get_dist(char1, char2):
            if char1 is None:
                return 0
            # Convert characters to coordinates in a 6-column grid
            c1, c2 = ord(char1) - ord('A'), ord(char2) - ord('A')
            return abs(c1 // 6 - c2 // 6) + abs(c1 % 6 - c2 % 6)

        # memoization dictionary
        memo = {}

        def solve(idx, other_pos):
            # Base case: word completed
            if idx == len(word):
                return 0
            
            state = (idx, other_pos)
            if state in memo:
                return memo[state]

            curr_char = word[idx]
            prev_char = word[idx - 1]

            # Option 1: Move the same finger that typed word[idx-1]
            res1 = get_dist(prev_char, curr_char) + solve(idx + 1, other_pos)

            # Option 2: Move the "other" finger to word[idx]
            # The previous finger now becomes the "other" finger for the next state
            res2 = get_dist(other_pos, curr_char) + solve(idx + 1, prev_char)

            memo[state] = min(res1, res2)
            return memo[state]

        # Start at index 1. The first character (index 0) is "free" for the first finger.
        # The second finger (other_pos) starts as None (also free).
        return solve(1, None)