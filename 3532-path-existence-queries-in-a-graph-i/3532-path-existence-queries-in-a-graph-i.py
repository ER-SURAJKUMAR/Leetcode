class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[bool]:
        # Array to store the component ID for each node
        component_id = [0] * n
        curr_id = 0
        
        # Group connected adjacent nodes into components
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                curr_id += 1
            component_id[i] = curr_id
            
        # Answer each query by verifying if they belong to the same component
        ans = []
        for u, v in queries:
            ans.append(component_id[u] == component_id[v])
            
        return ans