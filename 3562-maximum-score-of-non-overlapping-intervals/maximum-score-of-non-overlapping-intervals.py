from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)
        # Store original indices: (l, r, weight, original_idx)
        sorted_intervals = sorted(
            [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
        )
        starts = [interval[0] for interval in sorted_intervals]
        
        # dp[k][i] = (max_weight, lexicographically_smallest_indices_tuple)
        # Using 1-indexed for k up to 4
        dp = [[(0, ())] * (n + 1) for _ in range(5)]
        
        for i in range(n - 1, -1, -1):
            l, r, w, idx = sorted_intervals[i]
            # Find the first interval that starts strictly after r
            next_idx = bisect_right(starts, r)
            
            for k in range(1, 5):
                # Option 1: Skip the current interval
                best = dp[k][i + 1]
                
                # Option 2: Take the current interval
                next_weight, next_indices = dp[k - 1][next_idx]
                curr_weight = w + next_weight
                curr_indices = tuple(sorted((idx,) + next_indices))
                
                # Check if taking current interval yields a strictly better weight,
                # or equal weight with lexicographically smaller indices.
                if curr_weight > best[0] or (curr_weight == best[0] and curr_indices < best[1]):
                    best = (curr_weight, curr_indices)
                
                dp[k][i] = best
                
        return list(dp[4][0][1])