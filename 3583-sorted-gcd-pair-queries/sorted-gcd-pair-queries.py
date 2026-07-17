from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: list[int], queries: list[int]) -> list[int]:
        max_val = max(nums)
        
        # Step 1: Count frequencies of each number in nums
        freq = [0] * (max_val + 1)
        for x in nums:
            freq[x] += 1
            
        # Step 2: Count how many elements are multiples of each number i
        cnt_multiples = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            for j in range(i, max_val + 1, i):
                cnt_multiples[i] += freq[j]
                
        # Step 3: Compute the exact number of pairs with GCD equal to i
        # We process backwards to subtract counts from multiples
        exact_gcd_cnt = [0] * (max_val + 1)
        for i in range(max_val, 0, -1):
            c = cnt_multiples[i]
            total_pairs_divisible = c * (c - 1) // 2
            
            # Subtract pairs that have a strictly larger multiple of i as their GCD
            for j in range(2 * i, max_val + 1, i):
                total_pairs_divisible -= exact_gcd_cnt[j]
                
            exact_gcd_cnt[i] = total_pairs_divisible
            
        # Step 4: Create prefix sums of the exact GCD counts
        # prefix_sums[i] represents the total number of pairs with GCD <= i
        prefix_sums = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix_sums[i] = prefix_sums[i - 1] + exact_gcd_cnt[i]
            
        # Step 5: Answer each query using binary search
        ans = []
        for q in queries:
            # bisect_right finds the first index where prefix_sums[idx] > q
            idx = bisect_right(prefix_sums, q)
            ans.append(idx)
            
        return ans