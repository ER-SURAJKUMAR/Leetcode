class Solution:

  def minMoves(self, nums: list[int]) -> int:
    # Incrementing n - 1 elements by 1 is equivalent to decrementing 1 element by 1.
    # To make all elements equal, we need to bring all elements down to the minimum element.
    # Thus, the total moves equal the sum of differences between each element and the minimum element.
    return sum(nums) - min(nums) * len(nums)