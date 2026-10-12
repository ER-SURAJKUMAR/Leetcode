class Solution:

  def maxSum(self, nums: List[int], k: int) -> int:
    MOD = 10**9 + 7
    bit_counts = [0] * 31

    # Count the set bits at each position across all numbers
    for x in nums:
      for b in range(31):
        if (x >> b) & 1:
          bit_counts[b] += 1

    # Construct the k largest possible numbers
    res_nums = [0] * k
    for b in range(30, -1, -1):
      cnt = bit_counts[b]
      for i in range(min(cnt, k)):
        res_nums[i] |= 1 << b

    # Calculate the sum of squares modulo 10^9 + 7
    ans = 0
    for x in res_nums:
      ans = (ans + x * x) % MOD

    return ans