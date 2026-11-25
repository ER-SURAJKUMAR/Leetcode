class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        # Double rolling hash parameters
        MOD1, BASE1 = 1_000_000_007, 100_003
        MOD2, BASE2 = 1_000_000_009, 100_019

        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        pref1 = [0] * (n + 1)
        pref2 = [0] * (n + 1)

        for i, val in enumerate(nums):
            pow1[i + 1] = (pow1[i] * BASE1) % MOD1
            pow2[i + 1] = (pow2[i] * BASE2) % MOD2
            pref1[i + 1] = (pref1[i] * BASE1 + val) % MOD1
            pref2[i + 1] = (pref2[i] * BASE2 + val) % MOD2

        def get_hash(l: int, r: int) -> tuple[int, int]:
            # Hash of nums[l : r] (exclusive r)
            length = r - l
            h1 = (pref1[r] - pref1[l] * pow1[length]) % MOD1
            h2 = (pref2[r] - pref2[l] * pow2[length]) % MOD2
            return (h1, h2)

        def has_unique_of_len(length: int) -> bool:
            seen: dict[tuple[int, int], int] = {}
            for i in range(n - length + 1):
                h = get_hash(i, i + length)
                seen[h] = seen.get(h, 0) + 1
            return any(cnt == 1 for cnt in seen.values())

        lo, hi = 1, n
        ans = n
        while lo <= hi:
            mid = (lo + hi) // 2
            if has_unique_of_len(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans