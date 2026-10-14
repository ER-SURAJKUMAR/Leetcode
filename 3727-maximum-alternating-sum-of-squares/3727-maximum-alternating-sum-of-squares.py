class Solution:

  def maxAlternatingSum(self, nums: list[int]) -> int:
    nums.sort(key=abs)
    n = len(nums)
    mid = n // 2

    subtracted = nums[:mid]
    added = nums[mid:]

    return sum(x * x for x in added) - sum(x * x for x in subtracted)