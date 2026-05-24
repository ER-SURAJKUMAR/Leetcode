class Solution:
    def maxJumps(self, arr: list[int], d: int) -> int:
        n = len(arr)
        # dp[i] will store the maximum indices visited starting from index i
        dp = [-1] * n
        
        def dfs(i: int) -> int:
            # If already computed, return the cached result
            if dp[i] != -1:
                return dp[i]
            
            max_visited = 1 # We can always at least visit the starting index itself
            
            # Jump to the right
            for x in range(1, d + 1):
                j = i + x
                if j >= n:
                    break
                if arr[j] >= arr[i]: 
                    # Blocked by a taller or equal bar, cannot jump further right
                    break
                max_visited = max(max_visited, 1 + dfs(j))
                
            # Jump to the left
            for x in range(1, d + 1):
                j = i - x
                if j < 0:
                    break
                if arr[j] >= arr[i]:
                    # Blocked by a taller or equal bar, cannot jump further left
                    break
                max_visited = max(max_visited, 1 + dfs(j))
                
            dp[i] = max_visited
            return dp[i]
        
        # Try starting from every possible index and find the maximum
        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))
            
        return ans