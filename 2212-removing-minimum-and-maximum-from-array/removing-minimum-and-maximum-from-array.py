class Solution:

    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        # Find the 0-based indices of the minimum and maximum elements
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        # Identify which index appears first and which appears second
        i, j = min(min_idx, max_idx), max(min_idx, max_idx)

        # 1. Remove both from the front: index j + 1 deletions
        option1 = j + 1

        # 2. Remove both from the back: n - i deletions
        option2 = n - i

        # 3. Remove one from the front and one from the back: (i + 1) + (n - j) deletions
        option3 = (i + 1) + (n - j)

        return min(option1, option2, option3)