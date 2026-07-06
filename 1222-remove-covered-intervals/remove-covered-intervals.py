class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        # Sort by start ascending, then by end descending
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        remaining_count = len(intervals)
        max_end = 0
        
        for _, end in intervals:
            # If the current interval's end is within the max_end seen so far,
            # it is covered because its start is already >= previous start.
            if end <= max_end:
                remaining_count -= 1
            else:
                # Update the boundary for future checks
                max_end = end
                
        return remaining_count