import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        # Min-heap for free servers: sorted by (weight, index)
        free_servers = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(free_servers)
        
        # Min-heap for busy servers: sorted by (free_time, weight, index)
        busy_servers = []
        
        ans = [0] * len(tasks)
        curr_time = 0
        
        for j, task_time in enumerate(tasks):
            # Time can't be less than the task arrival time `j`
            curr_time = max(curr_time, j)
            
            # If no free servers are available, jump time to when the next server becomes free
            if not free_servers and busy_servers[0][0] > curr_time:
                curr_time = busy_servers[0][0]
                
            # Move all servers that have finished their tasks back to `free_servers`
            while busy_servers and busy_servers[0][0] <= curr_time:
                free_time, weight, index = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, index))
                
            # Assign the task to the top server in `free_servers`
            weight, index = heapq.heappop(free_servers)
            ans[j] = index
            
            # Push the server into `busy_servers` with its release time
            heapq.heappush(busy_servers, (curr_time + task_time, weight, index))
            
        return ans