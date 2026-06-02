class Solution:
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
        min_finish_time = float('inf')
        n = len(landStartTime)
        m = len(waterStartTime)
        
        # Iterate through all combinations of land and water rides
        for i in range(n):
            for j in range(m):
                # Scenario 1: Land ride first, then Water ride
                land_finish = landStartTime[i] + landDuration[i]
                water_start = max(land_finish, waterStartTime[j])
                total_time_1 = water_start + waterDuration[j]
                
                # Scenario 2: Water ride first, then Land ride
                water_finish = waterStartTime[j] + waterDuration[j]
                land_start = max(water_finish, landStartTime[i])
                total_time_2 = land_start + landDuration[i]
                
                # Update the minimum finish time found so far
                min_finish_time = min(min_finish_time, total_time_1, total_time_2)
                
        return min_finish_time