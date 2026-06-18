class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Minute hand moves 6 degrees per minute (360 / 60)
        minute_angle = minutes * 6
        
        # Hour hand moves 30 degrees per hour (360 / 12) and 0.5 degrees per minute (30 / 60)
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        
        # Find the absolute difference between the two angles
        diff = abs(hour_angle - minute_angle)
        
        # Return the smaller angle
        return min(diff, 360 - diff)