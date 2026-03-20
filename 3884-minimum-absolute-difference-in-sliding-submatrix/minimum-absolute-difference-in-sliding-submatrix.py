class Solution:
    def minAbsDiff(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        res_m, res_n = m - k + 1, n - k + 1
        ans = [[0] * res_n for _ in range(res_m)]
        
        for i in range(res_m):
            for j in range(res_n):
                # 1. Collect all elements in the k x k window
                elements = []
                for r in range(i, i + k):
                    elements.extend(grid[r][j : j + k])
                
                # 2. Get the SET of unique values and sort them
                unique_vals = sorted(list(set(elements)))
                
                # 3. If there are fewer than 2 distinct values, 
                # the problem notes the answer is 0.
                if len(unique_vals) < 2:
                    ans[i][j] = 0
                    continue
                
                # 4. Find the minimum difference between unique values
                min_diff = float('inf')
                for idx in range(len(unique_vals) - 1):
                    diff = unique_vals[idx+1] - unique_vals[idx]
                    if diff < min_diff:
                        min_diff = diff
                
                ans[i][j] = min_diff
                
        return ans