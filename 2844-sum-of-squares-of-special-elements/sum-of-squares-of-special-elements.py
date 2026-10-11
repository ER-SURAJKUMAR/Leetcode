class Solution:

  def sumOfSquares(self, nums: list[int]) -> int:
    n = len(nums)
    total_sum = 0
    # Since nums is 1-indexed in the description, we iterate from 1 to n.
    # In Python, 1-indexed position i corresponds to 0-indexed position i - 1.
    for i in range(1, n + 1):
      if n % i == 0:
        total_sum += nums[i - 1] ** 2
    return total_sum