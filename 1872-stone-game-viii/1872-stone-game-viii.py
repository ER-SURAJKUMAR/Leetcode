class Solution:

    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)

        # Compute prefix sums array
        # pref[i] represents the sum of stones[0...i]
        pref = [0] * n
        pref[0] = stones[0]
        for i in range(1, n):
            pref[i] = pref[i - 1] + stones[i]

        # Dynamic Programming with space optimization:
        # dp[i] represents the maximum score difference a player can achieve
        # when choosing to merge up to index i or further right (indices i to n - 1).
        # Base case: At the last possible move (i = n - 1), taking all stones gives pref[n - 1].
        dp = pref[n - 1]

        # Iterate backward from index n - 2 down to 1 (since x > 1, at least 2 stones must be taken)
        for i in range(n - 2, 0, -1):
            dp = max(dp, pref[i] - dp)

        return dp