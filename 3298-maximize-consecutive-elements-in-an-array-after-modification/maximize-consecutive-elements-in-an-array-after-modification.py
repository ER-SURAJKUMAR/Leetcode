from collections import defaultdict


class Solution:

    def maxSelectedElements(self, nums: list[int]) -> int:
        nums.sort()
        dp = defaultdict(int)
        ans = 0

        for x in nums:
            dp[x + 1] = dp[x] + 1
            dp[x] = dp[x - 1] + 1
            ans = max(ans, dp[x + 1], dp[x])

        return ans