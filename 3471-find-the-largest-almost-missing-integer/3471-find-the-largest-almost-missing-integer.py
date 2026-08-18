from collections import Counter
from typing import List


class Solution:

    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Case 1: k == 1 -> find max element that appears exactly once in nums
        if k == 1:
            freq = Counter(nums)
            ans = -1
            for num, count in freq.items():
                if count == 1:
                    ans = max(ans, num)
            return ans

        # Case 2: k == n -> only one subarray of size n exists, max element wins
        if k == n:
            return max(nums)

        # Case 3: 1 < k < n -> only nums[0] or nums[-1] can appear in exactly 1 subarray of size k
        # Count the number of subarrays of size k containing each distinct number
        subarray_counts = Counter()

        for i in range(n - k + 1):
            window = set(nums[i : i + k])
            for num in window:
                subarray_counts[num] += 1

        ans = -1
        for num, count in subarray_counts.items():
            if count == 1:
                ans = max(ans, num)

        return ans