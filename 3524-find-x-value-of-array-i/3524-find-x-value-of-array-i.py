class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        result = [0] * k
        dp = [0] * k  # dp[r] stores the count of subarrays ending at the current index with product % k == r
        
        for num in nums:
            val = num % k
            next_dp = [0] * k
            
            # Extend existing subarrays
            for r in range(k):
                if dp[r] > 0:
                    next_dp[(r * val) % k] += dp[r]
            
            # Start a new subarray consisting of only the current element
            next_dp[val] += 1
            
            # Accumulate results and update DP state
            for r in range(k):
                result[r] += next_dp[r]
            
            dp = next_dp
            
        return result