import bisect

class Solution:
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
        
        def get_min_total_time(first_start, first_dur, second_start, second_dur):
            n = len(first_start)
            m = len(second_start)
            
            # Pair and sort the second category by their start times
            second_rides = sorted(zip(second_start, second_dur))
            
            # Extract sorted start times for binary search
            sorted_starts = [ride[0] for ride in second_rides]
            
            # Precompute prefix minimums for durations
            # pref_min_dur[i] stores the min duration among second_rides[0...i]
            pref_min_dur = [0] * m
            curr_min = float('inf')
            for i in range(m):
                curr_min = min(curr_min, second_rides[i][1])
                pref_min_dur[i] = curr_min
                
            # Precompute suffix minimums for (start_time + duration)
            # suff_min_total[i] stores the min total time if we must wait for the ride to open
            suff_min_total = [0] * m
            curr_min = float('inf')
            for i in range(m - 1, -1, -1):
                curr_min = min(curr_min, second_rides[i][0] + second_rides[i][1])
                suff_min_total[i] = curr_min
            
            min_overall_finish = float('inf')
            
            # Iterate through each option for the first ride
            for i in range(n):
                finish_first = first_start[i] + first_dur[i]
                
                # Find how many second rides open before or at 'finish_first'
                idx = bisect.bisect_right(sorted_starts, finish_first)
                
                # Case 1: Choose a second ride that is already open
                if idx > 0:
                    min_dur = pref_min_dur[idx - 1]
                    min_overall_finish = min(min_overall_finish, finish_first + min_dur)
                    
                # Case 2: Choose a second ride that opens after 'finish_first'
                if idx < m:
                    min_overall_finish = min(min_overall_finish, suff_min_total[idx])
                    
            return min_overall_finish

        # Option A: Land ride first, then Water ride
        ans1 = get_min_total_time(landStartTime, landDuration, waterStartTime, waterDuration)
        # Option B: Water ride first, then Land ride
        ans2 = get_min_total_time(waterStartTime, waterDuration, landStartTime, landDuration)
        
        return min(ans1, ans2)