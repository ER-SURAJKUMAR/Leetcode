import bisect

class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[int]:
        # Extract unique sorted values
        unique_vals = sorted(list(set(nums)))
        m = len(unique_vals)
        
        # Map value to its index in unique_vals
        val_to_idx = {val: i for i, val in enumerate(unique_vals)}
        
        # Binary lifting tables: 18 levels are enough since n <= 10^5 (2^17 = 131072)
        LOG_MAX = 18
        up_right = [[0] * m for _ in range(LOG_MAX)]
        up_left = [[0] * m for _ in range(LOG_MAX)]
        
        # Initialize 2^0 lifts
        for i, x in enumerate(unique_vals):
            # For right: find largest y <= x + maxDiff
            r_idx = bisect.bisect_right(unique_vals, x + maxDiff) - 1
            if r_idx == i:
                up_right[0][i] = i  # Can't move forward
            else:
                up_right[0][i] = r_idx
                
            # For left: find smallest y >= x - maxDiff
            l_idx = bisect.bisect_left(unique_vals, x - maxDiff)
            if l_idx == i:
                up_left[0][i] = i  # Can't move backward
            else:
                up_left[0][i] = l_idx

        # Fill binary lifting tables
        for j in range(1, LOG_MAX):
            for i in range(m):
                up_right[j][i] = up_right[j - 1][up_right[j - 1][i]]
                up_left[j][i] = up_left[j - 1][up_left[j - 1][i]]
                
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            val_u, val_v = nums[u], nums[v]
            if abs(val_u - val_v) <= maxDiff:
                ans.append(1)
                continue
                
            idx_u = val_to_idx[val_u]
            
            if val_u < val_v:
                # Move right towards val_v
                steps = 0
                curr = idx_u
                # Lift to the furthest node that is still strictly less than a value 
                # capable of reaching val_v in 1 step (i.e., unique_vals[curr] + maxDiff < val_v)
                for j in range(LOG_MAX - 1, -1, -1):
                    nxt = up_right[j][curr]
                    if unique_vals[nxt] + maxDiff < val_v:
                        steps += (1 << j)
                        curr = nxt
                
                # Take one more greedy step from curr
                nxt = up_right[0][curr]
                if unique_vals[nxt] + maxDiff >= val_v and nxt != curr:
                    ans.append(steps + 2)
                else:
                    ans.append(-1)
                    
            else:
                # Move left towards val_v
                steps = 0
                curr = idx_u
                for j in range(LOG_MAX - 1, -1, -1):
                    nxt = up_left[j][curr]
                    if unique_vals[nxt] - maxDiff > val_v:
                        steps += (1 << j)
                        curr = nxt
                        
                nxt = up_left[0][curr]
                if unique_vals[nxt] - maxDiff <= val_v and nxt != curr:
                    ans.append(steps + 2)
                else:
                    ans.append(-1)
                    
        return ans